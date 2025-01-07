import streamlit as st

class FlowManager:
    """
    Controla el flujo de interacciones en la conversación.
    Permite avanzar paso a paso y verifica si se alcanzó el límite de interacciones.
    """
    def __init__(self, step, max_steps=10):
        # Inicializa el número máximo de pasos y el contador actual
        self.max_steps = max_steps
        self.current_step = step

    def can_continue(self):
        """
        Verifica si es posible continuar con las interacciones según el límite definido.
        """
        return self.current_step < self.max_steps

    def advance_local_step(self):
        """
        Incrementa el contador de pasos y lo sincroniza con st.session_state si no se ha alcanzado el límite.
        """
        if self.can_continue():
            self.current_step += 1
            st.session_state.step = self.current_step
        else:
            raise StopIteration("Se alcanzó el límite máximo de interacciones.")

    def reset(self):
        """
        Reinicia el contador de pasos y lo sincroniza con st.session_state.
        """
        self.current_step = 0
        st.session_state.step = self.current_step

    def finish(self):
        """
        Fija el contador de pasos al máximo permitido y lo sincroniza con st.session_state.
        """
        self.current_step = self.max_steps
        st.session_state.step = self.current_step

if __name__ == "__main__":
    
    # Prueba del FlowManager
    print("Iniciando prueba del FlowManager...")
    manager = FlowManager(max_steps=3)  # Configura un límite de 3 pasos

    try:
        while manager.can_continue():
            print(f"Paso actual: {manager.current_step + 1}")
            manager.advance_local_step()  # Avanza al siguiente paso
        print("Se completaron todas las interacciones permitidas.")
    except StopIteration as e:
        print(e)

    # Reinicia el flujo y muestra el estado
    manager.reset()
    print("FlowManager reiniciado.")
    print(f"Paso actual después del reinicio: {manager.current_step}")
