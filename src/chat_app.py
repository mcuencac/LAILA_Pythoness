import streamlit as st
import base64
from src.assistant import Assistant
from src.chat_history import ChatHistory
from src.flow_manager import FlowManager
from src.rag import RAG
from src.chat_history import ChatHistory
from src.utils.utils import get_env_key, BLUE, BRIGHT_WHITE, PASTEL_YELLOW, RESET

class ChatApp:
    """Clase principal que orquesta el funcionamiento de la aplicación."""
    def __init__(self):        
        
        self.assistant = Assistant()
        self.history = ChatHistory()
        self.initialize_session_state()  # Llamado al inicio para asegurar estado inicializado

        # Asignar valores desde session_state al objeto
        self.asking = st.session_state.asking
        self.info = st.session_state.info

        # Configurar el flujo del paso
        self.flow_manager = FlowManager(st.session_state.step, max_steps=6)
        self.step = self.flow_manager.current_step + 1

        # Cargar imágenes
        self.laila_avatar = self.load_image_as_base64("frontend/static/img/laila_avatar.webp")
        self.user_avatar = self.load_image_as_base64("frontend/static/img/user.png")

        # Definir los estados y acciones del flujo
        self.state_actions = {
            "INTRODUCTION": self.handle_flowstate_introduction,
            "QUESTION_1": self.handle_flowstate_question_1,
            "QUESTION_2": self.handle_flowstate_question_2,
            "PREPARE": self.handle_flowstate_prepare,
            "TAROT": self.handle_flowstate_tarot,
            "CLARIFICATIONS": self.handle_flowstate_clarifications,
            "FINISH": self.handle_final_response
        }

        self.rag = RAG()

    def initialize_session_state(self):
        """Inicializar todas las claves del estado de sesión en un solo lugar, incluyendo las tools."""
        defaults = {
            "app_initialized": False,
            "asking": None,
            "info": None,
            "step": 0,
            "flow_state": "INTRODUCTION",
            "welcome_shown": False,
            "messages": [],
            "disabled": False,
            "executing": False,  # Control estricto de ejecución
            "country_info": None,  
            "country_info_printed": False  
        }

        # Inicializar tools solo si no están ya registradas
        if "tools" not in st.session_state:
            st.session_state.tools = {
                "detect_country": self.assistant.detect_country_tool,
                "generate_welcome_message": self.assistant.generate_welcome_message_tool,
                "is_comprensible_message": self.assistant.is_comprensible_message_tool,
                "is_disrespectful": self.assistant.is_disrespectful_tool,
                "laila_tarot_reading": self.assistant.laila_tarot_reading_tool
            }

        # Inicializar las claves predeterminadas
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value

    def load_image_as_base64(self, path):
        """Carga una imagen y la convierte a base64."""
        with open(path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"

    def advance_local_step(self):
        st.session_state.step += 1

    def advance_flowstate(self, state):
        """Actualiza el estado del flujo tanto en la clase como en la sesión de Streamlit."""
        print(f"\n➡️ {BLUE} Actualizando estado:{RESET} {st.session_state.flow_state} >> {state}{RESET}")
        st.session_state.flow_state = state

    def handle_flowstate_introduction(self):
        """Manejador del estado INTRODUCTION."""   
        self.advance_local_step()     
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}")
        self.advance_flowstate("QUESTION_1")
        self.history.add_message("user", content=get_env_key('PROMPT_QUESTION_1'), hidden=True)
        self.laila_response(tone="solemne y cariñosa")

    def handle_flowstate_question_1(self):
        """Manejador del estado QUESTION_1."""
        self.advance_local_step()
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}")
        st.session_state.asking = self.history.get_messages()[-1]["content"]
        self.asking = st.session_state.asking
        print(f"\n{PASTEL_YELLOW}🦉 El usuario dijo (self.asking):{RESET} {self.asking}")
        valid_question = self.assistant.use_tool("is_valid_question", {self.asking})
        if valid_question:
            self.advance_flowstate("QUESTION_2")
            self.history.add_message("user", content=get_env_key('PROMPT_QUESTION_2'), hidden=True)
            self.laila_response()
        else:
            self.laila_response("impaciente")

    def handle_flowstate_question_2(self):
        """Manejador del estado QUESTION_2."""
        self.advance_local_step()
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}") 
        st.session_state.info = self.history.get_messages()[-1]["content"]
        self.info = st.session_state.info
        print(f"\n{PASTEL_YELLOW}🦉 El usuario dijo (self.info):{RESET} {self.info}")
        is_anything_else = self.assistant.use_tool("is_anything_else",{self.info},{self.asking})
        if is_anything_else:
            self.advance_flowstate("PREPARE")
            response = self.rag.ask_question("¿En que consiste la piramide invertida de 6 cartas?")
            # print(f"{BRIGHT_GREEN}Contexto: {response}{RESET}")
            self.history.add_message("system", content=response, hidden=True)  
            self.history.add_message("user", content=get_env_key('PROMPT_PREPARE'), hidden=True)
            self.laila_response("solemne")
        else:
            self.history.add_message("user", content=f"Lo que se te ha dicho no aporta informacion a la pregunta que fue: {self.asking}", hidden=True)
            self.laila_response("empatica pero impaciente.")

    def handle_flowstate_prepare(self):
        """Manejador del estado PREPARE."""
        self.advance_local_step()
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}")
        self.advance_flowstate("TAROT")
        last_message = self.history.get_messages()[-1]["content"]
        print(f"\n{PASTEL_YELLOW}🦉 El usuario dijo:{RESET} {last_message}")
        tirada = self.assistant.use_tool("laila_tarot_reading", self.asking, self.info)
        self.history.add_message("assistant", content=tirada, hidden=True)
        self.laila_reading(tirada)

    def handle_flowstate_tarot(self):
        """Manejador del estado TAROT."""
        self.advance_local_step()
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}")
        last_message = self.history.get_messages()[-1]["content"]
        print(f"\n{PASTEL_YELLOW}🦉 El usuario dijo:{RESET} {last_message}")
        self.laila_response("dramatica y solemne") 

    def handle_flowstate_clarifications(self):
        """Manejador del estado CLARIFICATIONS."""
        self.advance_local_step()
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}")
        last_message = self.history.get_messages()[-1]["content"]
        print(f"\n{PASTEL_YELLOW}🦉 El usuario dijo:{RESET} {last_message}")
        self.history.add_message("user", content=get_env_key('PROMPT_CLARIFICATIONS'), hidden=True)
        self.laila_response("empatica")       

    def handle_final_response(self):
        """Manejador del estado FINISH."""
        self.advance_local_step()
        print(f"\n{PASTEL_YELLOW}🔮 Interacción:{RESET} {self.step} {PASTEL_YELLOW}Paso activo:{RESET} {st.session_state.flow_state}")
        self.history.add_message("user", content=get_env_key('PROMPT_FINISH'), hidden=True)
        self.laila_response("dramática")

    def laila_response(self, tone="solemne", hidden=False):
        """Procesa y muestra la respuesta del asistente."""
        self.history.add_message("user", content=f"Sin perder tu habitual dramatismo místico y teatralidad, adoptas un tono {tone}", hidden=True)
        history = self.history.get_messages()
        response = self.assistant.client.get_response(history)
        if not hidden:            
            st.chat_message("assistant",  avatar=self.laila_avatar).markdown(f"{response}")
        self.history.add_message("assistant", content=response, hidden=hidden)
    
    def laila_reading(self, text):
        st.chat_message("assistant",  avatar=self.laila_avatar).markdown(f"{text}")
        self.history.add_message("assistant", content=text, hidden=False)

    def disable(self,value):
        st.session_state.disabled = value

    # def run(self):
    #     """Ejecuta la aplicación de chat."""
    #     if not st.session_state.app_initialized:
    #         st.session_state.app_initialized = True
    #         welcome_message = self.assistant.use_tool("generate_welcome_message")
    #         self.history.add_message("assistant", welcome_message)
    #         st.session_state.welcome_shown = True

    #     self.history.display_messages()
        
    #     # Inicializar el estado del botón deshabilitado
    #     if "disabled" not in st.session_state:
    #         self.disable(False)
        
    #     # Si ya terminó el flujo, deshabilitar la entrada
    #     if not self.flow_manager.can_continue():
    #         self.disable(True)

    #     prompt = st.chat_input("Escribe un mensaje...", disabled=st.session_state.disabled)
        
    #     if prompt and not st.session_state.disabled:            
    #         self.history.add_message("user", content=prompt)            
    #         st.chat_message("user", avatar=self.user_avatar).markdown(prompt)
        
    #     if self.flow_manager.can_continue():
    #         comprensible_message = self.assistant.use_tool("is_comprensible_message", self.asking)
    #         if comprensible_message:
    #             if not self.is_disrespectful(prompt):
    #                 current_state = st.session_state.flow_state
    #                 if current_state in self.state_actions:
    #                     self.state_actions[current_state]()
    #                 else:
    #                     st.error(f"Estado desconocido: {current_state}")
    #             else:
    #                 self.history.add_message("user", content="Se te ha ofendido gravemente", hidden=True)
    #                 self.history.add_message("user", content="Te despides dramatica y teatralmente y cierras la sesión hasta que reconsidere su lenguaje.", hidden=True)
    #                 self.laila_response("ofendida y teatral")
    #                 with st.container(key="ofended"):
    #                     st.write("🔮 Por favor, utiliza un lenguaje respetuoso. ")
    #         else:
    #             self.history.add_message("user", content=get_env_key('PROMPT_CHAT'), hidden=True)
    #             self.laila_response("excéntrica y teatral")
    #     else:
    #             print(f"\n{PASTEL_YELLOW}{RAISED_HAND} Finaliza el flujo{RESET}")
    #             self.flow_manager.finish()
    #             st.session_state.disabled = True
    #             self.history.add_message("user", content=get_env_key('PROMPT_CHAT'), hidden=True)
    #             self.laila_response("excéntrica y teatral")

    def run(self):
        """Ejecuta la aplicación de chat con control para evitar ejecución doble."""
        # Control estricto de inicialización
        if not st.session_state.get("app_initialized", False):
            st.session_state.app_initialized = True
            welcome_message = self.assistant.use_tool("generate_welcome_message")
            self.history.add_message("assistant", welcome_message)
            st.session_state.welcome_shown = True

        # Evitar doble ejecución con control explícito de reinicio
        if st.session_state.get("executing", False):
            return
        st.session_state.executing = True

        self.history.display_messages()

        # Finalizar si no se puede continuar
        if not self.flow_manager.can_continue():
            st.session_state.disabled = True
        else:
            st.session_state.disabled = False
        
        # Campo de entrada deshabilitado
        prompt = st.chat_input("Escribe un mensaje...", disabled=st.session_state.disabled)

        if prompt: 
            if not st.session_state.disabled:
                self.history.add_message("user", content=prompt)            
                st.chat_message("user", avatar=self.user_avatar).markdown(prompt)
                user_message = self.history.get_messages()[-1]["content"]
                comprensible_message = self.assistant.use_tool("is_comprensible_message", user_message)
                if comprensible_message:
                    disrespectful_message = self.assistant.use_tool("is_disrespectful", user_message)
                    if not disrespectful_message:
                        current_state = st.session_state.flow_state
                        if current_state in self.state_actions:
                            self.state_actions[current_state]()
                        else:
                            st.error(f"Estado desconocido: {current_state}")
                    else:
                        self.advance_local_step()
                        self.history.add_message("user", content="Se te ha ofendido gravemente", hidden=True)
                        self.history.add_message("user", content="Te despides dramatica y teatralmente y cierras la sesión hasta que reconsidere su lenguaje.", hidden=True)
                        self.laila_response("ofendida y teatral")
                        with st.container(key="ofended"):
                            st.write("🔮 Por favor, utiliza un lenguaje respetuoso. ")
                else:
                    self.advance_local_step()
                    self.laila_response("extrañada, confusa, impaciente y teatral")
            else:
                st.chat_message("user", avatar=self.user_avatar).markdown(prompt)
                user_message = self.history.get_messages()[-1]["content"]
                self.history.add_message("user", content=get_env_key('PROMPT_FINISH'), hidden=True)
                self.laila_response("excéntrica y teatral")
            
        # Reset para permitir futuras ejecuciones controladas
        st.session_state.executing = False

# Instanciar y ejecutar la aplicación
if __name__ == "__main__":
    app = ChatApp()
    app.run()