import re
from llm_agent import LLMAgent

class DocumentProcessor:
    def __init__(self, llm_agent, max_tokens, buffer=50):
        """
        Inicializa el procesador de documentos.
        :param llm_agent: LLMAgent, instancia para interactuar con el LLM.
        :param max_tokens: int, máximo de tokens permitido por llamada.
        :param buffer: int, margen de seguridad para evitar exceder el límite.
        """
        self.llm_agent = llm_agent
        self.max_tokens = max_tokens
        self.buffer = buffer

    def split_into_chunks(self, text):
        """
        Divide un texto en fragmentos procesables por el LLM.
        :param text: str, texto completo a dividir.
        :return: list, lista de fragmentos.
        """
        adjusted_limit = self.max_tokens - self.buffer
        words = text.split()
        chunks = []
        current_chunk = []
        current_length = 0

        for word in words:
            word_length = len(word) + 1  # Considera un espacio después de la palabra
            if current_length + word_length > adjusted_limit:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
                current_length = word_length
            else:
                current_chunk.append(word)
                current_length += word_length

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def process_document(self, document):
        """
        Procesa un documento grande utilizando el LLM.
        :param document: str, documento a procesar.
        :return: str, texto procesado combinado.
        """
        # Dividir el documento en fragmentos procesables
        chunks = self.split_into_chunks(document)

        # Procesar cada fragmento
        processed_chunks = []
        for i, chunk in enumerate(chunks):
            print(f"Procesando fragmento {i + 1}/{len(chunks)}...")
            prompt = f"""
            Limpia y estructura el siguiente texto que tiene algunos errores de ortografía y gramática, corrigelo para que sea más legible:

            {chunk}

            Responde unicamente con el texto corregido.
            """
            response = self.llm_agent.generate_response(role="user", prompt=prompt)
            processed_chunks.append(response)

        # Combinar los resultados procesados
        return "\n".join(processed_chunks)

# Ejemplo de uso
if __name__ == "__main__":
    # Documento de ejemplo
    raw_document = """
    
EL TAROT UNIVERSAL DE WALT E Edith Waite

EL TAROT UNIVERSAL DE WAI TE Edith Waite editorial i rio, s. a.

Un poco de historia El enigma del Tarot El Tarot esta rode a do de una rade en can to y de mister io, much om as que cu al quiero tro sistema a divina tori o. Qui en por primera vez tome en susman osu nj u ego de Tarot, sent ira una in descriptible a tracc ion haci a las im age-  nes plasma das en las cartas. Son fig uras que por un lado p are c en extra nias, pero que al mis-  mo tiempo hace niv br aral go en nuestro in te-  ri or. Es como si le hab laran direct a men teal alma, des per tando un cono cimi en to prof undo

El Tarot Universal de Waite 
e intemporal, olvidado durante mucho tiempo, aunque listo para 
surgir de nuevo a la superficie. 
¿Quién inventó estas cartas? ¿Cuándo? ¿Dónde? Y sobre 
todo: ¿con qué fin? 
En la actualidad, para ninguna de estas preguntas tenemos 
una respuesta. 
Toda historia tiene una parte externa, hasta cierto punto 
aceptada, estudiada y analizada; y otra oculta e insospechada, 
que jamás cronista alguno pudo registrar. Pocas veces ha sido 
esto tan evidente como en el caso del Tarot. Veamos un resu­
men de su historia externa. 
El significado de la palabra Tarot 
Su propio nombre es ya un misterio. La palabra «Tarot», usada 
en la actualidad en la mayoría de los idiomas, es el término 
francés que denomina al «tarocco», juego que -hasta donde 
sabemos- apareció por primera vez en el norte de Italia a prin­
cipios del siglo XV y que está compuesto de 78 cartas, formadas 
por 22 «triunfos» o Arcanos Mayores y 56 menores, que a su vez 
están divididos en cuatro especies o palos: oros, copas, espadas 
y bastos. Ya en el año 1550, Flavio Alberti Lallio se preguntaba 
cómo era posible que la extraña palabra «tarocco» careciera de 
etimología. Es extraordinario que no exista referencia alguna a 
esta palabra antes de que el juego haga su aparición. Parece que 
en un principio se lo denominó «triunfos» o «cartas con triunfos», 
pues no consta ninguna referencia escrita a la palabra «tarocco» 
hasta el año 1516. 
Las teorías acerca del origen de la palabra Tarot son muy 
abundantes, la mayoría de ellas de tipo esotérico. Unos creen 
que procede del término Tara, frecuente en las tradiciones y los 
mitos de diferentes pueblos antiguos, entre ellos, en el tantrismo 
8

un poco de historia 
tibetano. Quienes atribuyen al Tarot un origen egipcio, hacen 
derivar su nombre de las palabras egipcias Ta-Rosh, que signifi-
can «el estilo, o el camino real». Los que creen que el Tarot fue 
compuesto por cabalistas no pueden dejar de notar la similitud 
de las palabras Tarot y Torah, nombre dado por los hebreos a los 
cinco primeros libros del Antiguo Testamento. Para otros la pala-
bra Tarot es un anagrama del vocablo latino Rota, que significa 
rueda, haciendo referencia al continuo cambio que prevalece en 
este mundo, conectándose al mismo tiempo con la tradición 
hindú de la rueda de la vida y con el I Ching o libro de los cam-
bios chino. Curiosamente, las cinco letras de la palabra Tarot 
contienen las tres del Tao (el camino), siendo éste también el 
significado de la palabra árabe Tariqa, etimología preferida por 
quienes sostienen la teoría de que el Tarot fue compuesto por un 
grupo de sabios del norte de África. Por si esto fuera poco, en la 
zona del norte de Italia, de donde proceden las primeras refe-
rencias históricas al Tarot, hay un río denominado Taro, nombre 
que según algunos se habría dado al juego, inspirado en ciertas 
cartas orientales traídas por los mercaderes que llegaban a 
Venecia (en aquella época la ciudad de Venecia centralizaba 
todo el comercio con Asia). 
Pero la realidad es que hasta el día de hoy el origen de su 
nombre, como el origen del propio Tarot, sigue oculto tras el 
más profundo de los misterios. 
Los primeros datos históricos 
Aunque los primeros juegos de cartas surgieron al parecer en 
China alrededor del siglo X de nuestra era, está por demostrar 
que tuvieran alguna semejanza con el Tarot o con los juegos de 
cartas europeos. De hecho, las primeras referencias histórica-
mente comprobadas sobre el Tarot proceden de mediados del 
9

10
El Tarot Universal de Waite
siglo XV. Un manuscrito religioso fechado a finales de dicho siglo 
incluye el sermón de un sacerdote franciscano que, alrededor 
del año 1450, arremete en la Umbría italiana contra los juegos 
en general, calificándolos de invención diabólica, y menciona 
específicamente tres: los dados, las cartas y los «triunfos». Los 
juegos de cartas eran ya populares al menos desde cien años 
antes y las referencias históricas abundan: en el año 1332 
Alfonso XI, rey de Castilla y León, prohibió a sus caballeros 
entretener su ocio jugando a las cartas. En 1377, un monje sui-
zo hace una detallada descripción del juego de cartas y de sus 
cuatro «palos» –oros, copas, espadas y bastos– pero no hace 
referencia a los «triunfos» (hoy Arcanos Mayores). En el año 
1480, un autor llamado Covelluzo dice que las cartas habían lle-
gado a Italia en el año 1379, traídas por los árabes del norte de 
África, pero sin precisar tampoco si en ellas iban incluidos los 
Arcanos Mayores. Un documento de la corte del rey Carlos VI 
de Francia (1380-1422), fechado en el año 1392, registra un 
pago realizado al pintor Jacquemin Gringoneur por «tres juegos 
de cartas coloreados y adornados», pero se desconoce si dichos 
juegos incluían también los «triunfos» (curiosamente en el mismo 
año de 1392 el rey Carlos VI se volvió loco). La gran populari-
dad que el juego de cartas había alcanzado ya a mediados del 
siglo XV, entre todas las clases sociales, queda evidenciada por 
la orden emitida por el alto magistrado de Venecia en el año 
1441, prohibiendo la importación de barajas a fin de proteger la 
producción local. El Parlamento inglés promulgaría una ley simi-
lar en el año 1464.
Sin embargo, el citado sacerdote franciscano es el primero 
que menciona los «triunfos», y además da sus nombres, que son 
bastante parecidos a los actuales Arcanos Mayores: el bagatello, 
imperatrix, imperator, la papesa, el papa, la temperantia, l’amore, il 
carro triunfale, la forteza, la rotta, el gobbo, lo impichato, la morte, 
el diavolo, la sagitta, la stella, la luna, el sole, l’angelo, la iustizia, el

11
Un poco de historia

12
El Tarot Universal de Waite

13
Un poco de historia

14
El Tarot Universal de Waite
Nadie sabe en la actualidad el significado de las letras que 
identifican a cada una de las cinco series, pero es ciertamente 
muy curioso que veintidós de las cartas de Mantegna tengan un 
parecido notable con dieciséis cartas del Tarot, trece Arcanos 
Mayores y tres Menores. ¿Nació y evolucionó el Tarot como un 
producto autóctono del norte de Italia, o llegó procedente de 
otras tierras, adaptándose luego e influyendo a otros juegos de 
cartas como el de Mantegna?
El Tarot y los gitanos
La teoría de que el Tarot llegó a Europa traído por los gitanos 
fue mantenida con vehemencia durante siglos. Éstos comenza-
ron a llegar a suelo europeo procedentes del Asia central a par-
tir del año 1411, por lo que cronológicamente ello sería factible, 
pero no hay un solo indicio que apoye esta teoría –ni tampoco 
ninguna otra, en lo que al origen del Tarot se refiere–. La afición 
adivinatoria de los gitanos parece corroborarla, aunque, de nue-
vo, no existe ninguna referencia escrita y además, las artes adi-
vinatorias de los gitanos suelen orientarse hacia otros campos, 
básicamente la lectura de las líneas de la mano. Sin embargo el 
ocultista francés Papus dice en su libro El Tarot de los Bohemios:
Los bohemios poseen una biblia, esta biblia les facilita el 
diario vivir, pues con ella predican la buenaventura; esta 
biblia es también un motivo continuo de ocio, puesto que 
les permite entretenerse jugando.
Sí, ese juego de cartas denominado Tarot, que poseen los 
bohemios, es la biblia de las biblias. Es el libro de Toth-
Hermes-Trismegisto, es el libro de Adán, es el libro de la pri-
mitiva revelación de las antiguas civilizaciones.

15
Un poco de historia

El Tarot Universidad de Waite 
16 
algo muy diferente del simple juego de cartas que hasta enton­
ces había sido. 
Corría el citado año de 1775, cuando a Antoine Court de 
Gébelin -erudito, sacerdote protestante y francmasón- le 
enseñaron una baraja del otrora popular juego, que para enton­
ces estaba ya totalmente olvidado. Al serle mostradas una a una 
las cartas del Tarot de Marsella, Court de Gébelin se sintió 
automáticamente fascinado por ellas y de pronto su simbolismo 
se perfiló muy claro en su mente. Dedujo por intuición que se 
trataba de un antiguo libro egipcio, cuyos dibujos contenían 
todo el saber de dicha civilización ya extinta, y lo atribuyó al 
poderoso dios egipcio Thoth. Posteriormente recopiló sus traba­
jos sobre el Tarot en un libro que tituló Le Jeu des Cartes. 
La gran reputación de Court de Gébelin hizo que sus ideas 
sobre el Tarot se popularizaran con rapidez, a lo cual contribuyó 
mucho un vidente y adivino profesional que se hacía llamar 
«Etteilla» (transposición de su apellido real: Alliette). Etteilla era 
un enamorado de los temas egipcios, por lo que adoptó el Tarot 
como instrumento adivinatorio y apoyó totalmente la teoría de 
su origen, adornándola con nuevos detalles de su cosecha, 
como la fecha de su creación (171 años después del diluvio) y la 
identidad de sus creadores (lo compusieron 17 magos bajo las 
órdenes directas de Hermes Trismegisto, en un templo distante 
tres leguas de Menfis). Lamentablemente, cuando dieciocho 
años después, gracias a la piedra Rosetta, se pudieron traducir la 
mayoría de los jeroglíficos egipcios, no apareció en éstos ningu­
na referencia al Tarot, pero no por esto perdió fuerza la teoría de 
su origen egipcio; además, la idea, común durante siglos, de que 
los gitanos procedían de Egipto siguió de algún modo apoyan­
do dicha creencia. 
Lo notable es que gracias a Court de Gébelin el Tarot dejó 
de ser un simple y olvidado juego de cartas para convertirse en 
algo mucho más serio y trascendente, cargado ahora con una 
aureola de profundidad, de misterio y de esoterismo.

17
Un poco de historia

El Tarot Universidad de Waite 
El Tarot es de hecho una máquina filosófica, que evita que 
la mente divague, manteniendo al mismo tiempo toda su 
iniciativa y su libertad. Es las matemáticas aplicadas a lo 
Absoluto. Es la alianza de lo positivo y lo ideal. Es una 
lotería de pensamientos tan exactos como los números. Tal 
vez estemos ante la más grande y más sencilla creación del 
genio humano en todos los tiempos. Alguien encerrado en 
una celda, sin otro libro que el Tarot, puede, en pocos años 
-si sabe cómo usarlo-, adquirir todo el conocimiento uni­
versal y ser capaz de hablar sobre cualquier tema con ini­
gualable precisión y elocuencia. 
La emoción de Eliphas Lévi se comprende si tenemos en 
cuenta que, desde el punto de vista cabalístico, el alfabeto 
hebreo es algo más que un simple sistema de escritura: es una 
expresión de todos los hechos y de todas las fuerzas de la crea­
ción, organizadas en la estructura conocida como el Árbol de la 
Vida, compuesta por diez esferas o Sephiroth, las cuales están 
conectadas por veintidós senderos de sabiduría, cada uno de 
ellos designado por una letra hebrae. Eliphas Lévi asignó cada 
uno de los 22 Arcanos Mayores del Tarot a los 22 senderos del 
árbol y posteriormente acomodó también los Arcanos Menores, 
creando así un sistema completo que integraba el número, la 
palabra y la imagen. Esta síntesis había sido durante siglos el 
gran sueño de los investigadores esotéricos. 
18

L in poco de historia 1 Kether 3 2 Bin ah Chok mah 5 4 Gebura h Che sed 6 Tif are th 8 7 Hod Net zah 9 Yes od 10 M alkut ElA rb old ela Vida 19

20
El Tarot Universal de Waite
Con el tiempo, los 22 Arcanos Mayores han sido asignados 
a los 22 senderos del Árbol de la Vida de formas diferentes. La 
siguiente es una de las más usuales:

21
Un poco de historia
El Tarot a finales del siglo XIX. Papius
Las ideas de Eliphas Lévi fueron recogidas y ampliadas por 
otros ocultistas posteriores, entre ellos Paul Christian, quien en 
1863 publicó El hombre rojo de las Tullerías, obra que ejercería 
gran influencia sobre varias generaciones de ocultistas. Aunque en 
ella el Tarot no es nombrado jamás, las alusiones son abundantes: 
Christian describe, por ejemplo, un gran círculo formado por 
setenta y ocho láminas de oro, que una vez estuvieron ocultas en 
un templo de Menfis, cumpliendo cada una de ellas una función 
específica en el proceso de iniciación a los antiguos misterios.
En el año 1888 ocurrieron dos hechos que tendrían gran 
trascendencia en la historia del Tarot: el marqués Stanislas de 
Guaita y el Dr. Gérard Encausse (Papus) fundaron la Orden 
Cabalística de la Rosa Cruz. Un año después Guaita y el pintor 
Oswald Wirth produjeron una versión revisada del Tarot clásico, 
que sigue editándose en la actualidad. Al mismo tiempo, Papus 
publicaba su obra El Tarot de los bohemios. Seguidor de Eliphas 
Lévi, Papus elaboró y refinó las ideas esbozadas por éste y su 
obra se compone básicamente de interpretaciones cabalisticas 
del Tarot y de fundamentos de tipo mágico. Papus llevó un paso 
más allá lo dicho por Court de Gébelin sobre el origen del Tarot. 
Según él, los sacerdotes egipcios decidieron deliberadamente 
dar a sus secretos la apariencia de un juego:
Inicialmente los sacerdotes pensaron que estos secretos 
debían ser confiados a un grupo de hombres virtuosos, 
reclutados en secreto por los propios iniciados, para que 
los transmitieran de generación en generación. Pero uno 
de los sacerdotes, dándose cuenta de que la virtud es cosa 
muy frágil y muy difícil de hallar, propuso confiar sus tradi-
ciones científicas no a la virtud, sino al vicio. El vicio, según 
él, nunca desaparecerá totalmente, por ello a través de él, 
podía asegurarse la permanencia de los principios que ellos

El Tarot Universal de Waite quer ian transmit ira la poster id ad. Evident e men tel a opi ni on de este sacer do te fue la que preva le cio y pore ll ose esc ogi o un jue go. En t once s grab a ron pe que nias plan chas con las mi st erios as fig ur as que represent an los mas imp or-  t antes secret osc i ent if ico s, yas if los jug adores de cart as han transmit ido ese Tarot degener aci one ngener aci on, mucho mejor del o que lo hub i er an podido h acer los hombres mas vi r tuo sos.  Aunque, en real i dad, El Tarot delos boh emi ose s mas un libro de magia que de Tarot, la metic u los id ad de Papus al argu-  ment ary a pay arca da una des us afirma ci ones lo hace de st a-  cars e entre las num eros as obras de o cult is mo public adas en Francia en la segunda mit add el sig loX IX.  Crea cio ndel Tarot modern o. La Golden Dawn Elo tros u ce so important eoc urdi oen 1888 fue la crea cio ndel a Or den Her met ica dela Aurora Dorada( The Hermetic Order of the Golden Dawn) . Fund ada en Lond res por un notable grupo en el que se hall a ban no solo a fico nado salama g is in over da-  deros eru di to s, como William Butler Yeats( premio Nobel de Liter a tura) y Gerald Kelly( posterior men te presidente dela Real Academia) , la Golden Dawn dura tans lo uno sano s, pero su in flue nci as sobre elo cult is mo del sig loX X has ido imp res ion an te y, de he cho, sig uel leg ando a nuestros dias.  Uno delos fund adores dela Golden Dawn, el Dr. Wy n We scott, entr oen contact oc on Samuel Liddell Mathers( que l ue-  go se hi zo llamar Mac Gregor Mathers) , qui en ha bia escrito un libro de adiv in aci on sobre el Tarot, y lo in vit o a uni rise a la rec ien c read a sociedad. Pronto, Mac Gregor Mathers se convirt i oen la principal fue rza impuls orade la Golden Dawn yen su teo rico 22

un poco de historia 
más prominente. Dotado de un gran ingenio y de notable caris-
ma, exéntrico y autoritario, Mathers fue el autor de la mayoría 
de los rituales mágicos de la orden. Bajo su liderazgo la Golden 
Dawn creó un sistema mágico moderno, que integraba de un 
modo coherente diferentes disciplinas: la cábala, el Tarot, la 
alquimia, la astrología y la numerología, junto a la experiencia 
visionaria y la magía ritual. Los miembros de la Golden Dawn 
eran buscadores serios, que debían realizar un impresionante 
trabajo, pasando por una serie de iniciaciones cada vez más 
complicadas, estudiando las diversas materias citadas, tomando 
parte en rituales y tratando de lograr visiones espirituales. 
Además, debían llevar un diario, detallando en él todas sus 
experiencias, y sobre todo debían meditar diariamente sobre las 
imágenes del Tarot. 
En la Golden Dawn el Tarot adquirió un contexto esotérico 
que nunca antes había tenido. Se lo relacionó coherentemente 
con casi todas las tradiciones antiguas y, lo que es más impor-
tante, fue usado de un modo muy creativo. Cada miembro 
debía dibujar su propio Tarot, basándose en las instrucciones 
que recibían de la orden. Los triunfos o Arcanos Mayores (que 
entonces pasaron a llamarse «claves») fueron considerados 
como puertas a través de las cuales la imaginación penetraba en 
niveles profundos e inmateriales del ser. A las diferentes cartas se 
les asignaron distintos «grados» o niveles y eran utilizadas pro-
fusamente en numerosos rituales e iniciaciones. 
Disolución de la Golden Dawn 
Hacia el año 1900, en el seno de la Golden Dawn habían surgi-
do ya varias facciones que cada vez eran más fuertes y divergen-
tes. Mathers vivía entonces en París con su esposa Moina (herma-
na del filósofo Henri Bergson) y desde allí trataba de controlar a 
23

24
El Tarot Universal de Waite
los miembros de Londres a través de cartas y envíos, pero su 
autoridad real decaía sin remedio. Parece que en un intento por 
recuperar su posición anterior difundió la especie de que 
Wescott había falsificado un importante documento relativo a la 
fundación de la orden. Esto enrareció todavía más el ambiente 
y precipitó las cosas. Yeats, que sufrió enormemente con aque-
llos escándalos, escribía en una carta confidencial a su amiga 
Lady Gregory:
Últimamente lo he pasado muy mal. Ya te dije que había-
mos sacado a MacGregor de la Kabbala. Bueno, pues la 
semana pasada ha mandado a un loco –al que tiempo atrás 
nos negamos a dar la iniciación– para que tomara posesión 
de los bienes y de los documentos de la sociedad...
El «loco» en cuestión no era otro que Aleister Crowley, 
miembro de la orden «externa» y a la sazón joven protegido por 
Mathers. Crowley, disfrazado con una túnica celta y con una 
máscara negra en el rostro, trató de tomar posesión de los docu-
mentos y de la parafernalia de la sociedad y tuvo que ser saca-
do a la fuerza por los guardias. Según palabras de Yeats la ini-
ciación y el paso al círculo «interno» le habían sido denegados 
«porque se supone que la Golden Dawn es una sociedad misti-
ca, no un manicomio».
Este episodio precipitó todavía más la desintegración de la 
orden, de cuyos restos surgieron luego numerosas sociedades 
esotéricas, algunas de las cuales siguen funcionando en la actua-
lidad. Dado que el Tarot había sido uno de los temas más estu-
diados de todo su sistema, cada uno de dichos grupos creó lue-
go su propio Tarot, «perfeccionando» el de la Golden Dawn, y 
por supuesto un libro o varios interpretándolo. De este modo, la 
disolución de la Golden Dawn originó un crecimiento y una 
difusión del Tarot todavía mucho mayores de lo que nunca antes 
había tenido.

El Tarot de Waite 
De entre los tarots que surgieron de las cenizas de la Golden 
Dawn, el creado por Arthur Edward Waite es el más significati-
vo. Sin duda es el más conocido de todos los tarots modernos y, 
casi cien años después, sigue siendo también el más difundido. 
Waite era un estudioso que había traducido al inglés, entre otras, 
las obras de Papus y de Eliphas Lévi y que en 1903 se hizo car-
go del templo londinense de la Golden Dawn, infundiéndole en 
el acto una orientación más mística que mágica. Yeats y un nutri-
do grupo de miembros que preferían el sendero de la magia ini-
ciado por MacGregor Mathers se separaron entonces, creando a 
su vez la orden Stella Matutina. 
Waite estaba decidido a corregir los muchos malentendidos 
y especulaciones que existían acerca del Tarot, por lo que en su 
obra La clave pictórica del Tarot, publicada en 1910, denuncia 
el origen egipcio del mismo, junto con otras fantasías seudo-
históricas muy difundidas. De hecho, puso al Tarot bajo una luz 
totalmente nueva y marcó la pauta para gran parte de lo que 
sería escrito sobre este tema durante todo el siglo XX: 
El Tarot es una representación simbólica de ideas universa-
les, en las cuales está basada la mente y el comportamien-
to humano y, en este sentido, contiene una doctrina secre-
ta, a la cual es posible acceder, pues de hecho está ya en la 
conciencia de todos nosotros, aunque el hombre ordinario 
pase por la vida sin reconocerla. Esta doctrina ha existido 
siempre, es decir, siempre ha habido una minoría capaz de 
acceder a ella, y ha sido registrada y transmitida a través de 
obras y tradiciones secretas como la Alquimia y la Cábala. 
Una importante contribución de Waite a la interpretación 
del simbolismo del Tarot fue la inclusión de la alquimia, junto a 
la cábala. Para Waite la alquimia era un proceso psicológico y 
25

26
El Tarot Universal de Waite
espiritual en el que la finalidad del adepto sería purificar su ser 
interno y lograr niveles de conciencia cada vez más elevados. El 
Tarot diseñado por él y dibujado por Pamela Colman Smith fue 
publicado en 1910 por la empresa Rider & Co. (de ahí el nom-
bre Rider-Waite por el que también se lo conoce). Una de las 
muchas innovaciones introducidas por Waite, y que serían ya 
seguidas por casi todos los Tarots posteriores, es la inclusión de 
escenas y paisajes en los Arcanos Menores.
El Tarot universal es una actualización del Tarot de Waite, 
en la que se han avivado los colores y se ha incrementado el 
detalle de las ilustraciones, se han añadido las letras hebreas en 
los Arcanos Mayores y se han modificado algunos detalles, intro-
duciendo otros también procedentes de la Golden Dawn, a fin 
de resaltar algún punto de la simbología. Igualmente, muchos de 
los comentarios de este libro –sobre todo los adivinatorios– acer-
ca de las diferentes cartas están basados en las enseñanzas de la 
Golden Dawn.
El Tarot de Crowley
Si bien el nombre de Waite es conocido por todos los interesa-
dos en el Tarot, el alumno más famoso de la Golden Dawn es sin 
duda el ya mencionado Aleister Crowley (autoapodado «la Gran 
Bestia», «Frater Perdurabo» y el «Maestro Therión»). En su vida 
abundó la excentricidad y el escándalo –en sus rituales mágicos, 
por ejemplo, las drogas y el sexo no eran ingredientes extraños–, 
sin embargo fue un serio estudioso del esoterismo, muy percep-
tivo y con una gran imaginación. En el año 1938 Lady Frieda 
Harris le pidió trabajar con ella en un Tarot que pensaba diseñar, 
influida por la lectura del libro de Ouspenski Un nuevo modelo 
de Universo (en el que Ouspenski describe con detalle sus ideas y 
sus teorías sobre el Tarot, básicamente bajo un enfoque cristiano).

Un poco de historia La cola bora cio n entre Harris y Crowley dur ose is anos yel resul-  tado fue un Tarot muy llam at ivo y total men te dist into a los ex is-  ten tes has ta en t once s, con una rica simo logia pro cede n te dela cabal a, la fran cmas one ria, los ros a cruces, la magi a, la al quim i a,  la psi co logia, el bud is mo, la astro logia, la quim i cay las mate ma-  ticas, porc it ars olo al gun as del as tr adic i ones y del as ciencia s.  Enel a no 1944- un an o antes dela muerte de Crowley- se imp rmi eric on solo 200 ejempl are s, no si endo real men te edit a do has tae la no 1969.  Tambi en en 1944 Crowley public osu o bra maestra El Libro de Thoth, en la que exp lica su Tarot con una sens at ez y una original i dad que to davi as or pre nden as us detract ores.  Seguin el, el Tarot deb fae n tender se como una represent aci on pictor ica del as fue rz as dela Naturaleza, tal como las con ce bif an los hombres dela anti gue d adys e gun el sim bol is mo conv en cio nal. Es bast ante ironi co que Crowley titular as uob rae l Libro de Thoth, pu es leno crea que hub ie sev in cul o his to rico al gun o entre el Tarot y la anti gua civil i zac ion eg ip cia,《 in clu so en caso de que lle gara a cono cer se, el origen del Tarot care ce total men te de import an cia, dice en la intro duccio n.  Las ideas de Crowley sobre el Tarot er an basic a men tel as dela Golden Dawn, en rique c id as con los nuevo s descubrimien-  to s cie nti fic os- tanto en el campo dela f is ica como dela nueva psi co logia deC. G. Jung- para el el Tarot era un instrument o simb o lico, cu yau t it i zac ion pr act ica podia convert irs een un sen-  derode cono cimi en to, de transform aci on y de il umina ci on.  Otros here deros dela Golden Dawn: el Tarot de BOT A Todos los Tarots mencion a dos has tara hora y los person a jes his to ricos re lac iona dos con ello s son marc adam en te europe os.  Pero haci a later cera de cad a del sig loX X eles piri tu american o 27

28
El Tarot Universal de Waite
irrumpió también en el mundo del Tarot. Las sociedades secre-
tas, las referencias veladas y los aristócratas exéntricos fueron 
poco a poco cediendo su lugar a organizaciones totalmente 
prácticas, que no dudaron en emplear para sus fines los mismos 
medios que compañías como la Ford o la General Motors utili-
zaban para incrementar sus ventas cada año.
Tal vez la figura más significativa de esta época sea Paul 
Foster Case. De joven trabajó en el teatro como ilusionista y 
mago, siendo las cartas uno de sus instrumentos preferidos. 
Posteriormente sus estudios sobre el Tarot lo llevaron ante el 
capitolio neoyorquino de la Golden Dawn, donde fue admitido 
en el año 1910. Pocos meses después falleció el líder, y Paul 
Foster Case fue nombrado para sustituirlo, pasando así a con-
vertirse en la máxima autoridad de la Golden Dawn en Estados 
Unidos y Canadá; sin embargo su relación con dicho grupo se 
fue poco a poco deteriorando hasta que finalmente, en el año 
1920, Case formó su propia escuela a la que llamó Cons-
tructores del Adytum, más conocida como BOTA por sus inicia-
les en inglés (Builders of the Adytum).
Paul Foster Case publicó su libro El Tarot en 1927 y El Tarot 
de BOTA en 1931, siendo éste muy parecido al de Waite, aun-
que con la particularidad de que los dibujos son en blanco y 
negro, a fin de que el usuario los pueda colorear personalmen-
te, algo parecido a lo que se hacía en la Golden Dawn. En el año 
1933 Case trasladó BOTA a Los Ángeles, donde construyó un 
colorido templo dedicado al Tarot y a la cabala, desde el cual 
comenzó a difundir cursos por correspondencia a todo el mun-
do, los cuales siguen impartiéndose con notable éxito en la 
actualidad, en varios idiomas.
Paul Foster Case hizo también su aportación a los ya 
numerosos mitos sobre el origen del Tarot, creándole, o al 
menos difundiendo, un nuevo escenario:

un poco de historia Seg u nuna ci ert a tr adic ion o cult a, haci a la cu al me inc lino,  en real i dad el Tarot fue invent a do haci a ela no 1200 de nuestra era, por un grupo de adeptos ques ere un if an period i came ten la ciudad de Fez, en Marrue cos. Tr asla des-  tru cci on de Ale j and ria, Fez se con vi rti oen la capital cie nti-  fic a y liter aria del mundo. All ile gaba nsa bios de todos los países, cad a uno hab lando suprop i alen gua, por lo ques us reunion essec o mica ban a causa del as diferent i cas de len-  gua jey de termino logia filos of ica. Por ello, crea ron un in s-  tru men to que in clu y era las mas important es de sus do c tri-  nas, en la form a de un libro de im a genes, cu ya comb in a-  ci 6 nde pendi ese dela oculta ar moni a delos num eros.  Aunque total men te bas a do en las ense nia nz as dela Golden Dawn, el en fo que de Paul Foster Case sobre el Tarot es nuevo y fresco, en parte por que jun to alas asoci aci ones cabal is ticas de cad a uno delos Arcano s May ores( llamado s tambi en《 claves》  como en la Golden Dawn) in clu y eun a inter es an te dimension p sico logica en la que in corpora last e or i as de Freud y de Jung,  d and olea dem as al estudio del as cartas un aspect om as a bier to, mas america no. Case, que muri oen elan o 1954, fue sus ti-  tui do al frente de BOT A por An n Davies.  El Tarot en la segunda mit adde l sig lox x Dos estudi osos del Tarot pro cede n tes tambi end ela Golden Dawn que mere c en ser men c iona dos son Manly P. Hall e Israel Regard ie. El prime rode ello s public o un Tarot enel a no 1930,  bas a do en el deOs wald Wi rth. En suo braUn ens a yo sobre el Tarot dice Manly P. Hall:

30
El Tarot Universal de Waite
Las cartas no pueden explicarse tan sólo estudiando los 
propios jeroglíficos, pues sus símbolos han pasado por 
muchas fases y modificaciones. Una generación tras otra 
ha rediseñado el Tarot, hasta finalmente dejar muy poco 
del original. El estudiante debe ver más allá de las cartas y 
debe tratar de descubrir la psicología que las produjo. 
Como cualquier otra forma de simbolismo, el Tarot refleja 
inevitablemente el punto de vista de quien lo interpreta. 
Esto no disminuye su valor, pues el simbolismo es uno de 
los instrumentos más prácticos en el aprendizaje de las 
artes espirituales, ya que extrae de los recursos subjetivos 
del buscador la sustancia de su propia erudición.
Israel Regardie fue miembro de la Golden Dawn –en su 
última fase– y discípulo de Aleister Crowley. Tras romper con 
éste en 1934 se trasladó a California, donde publicó cuatro volú-
menes sobre los documentos de la Golden Dawn, revelando por 
primera vez al público los detalles de sus rituales y de sus prac-
ticas. Tanto Manly P. Hall como Israel Regardie vivieron y siguie-
ron publicando libros hasta finales de la década de los ochenta.
A partir de 1970 las obras sobre el Tarot y los nuevos 
diseños de Tarots han proliferado de manera sorprendente, sien-
do en general la calidad casi tan notable como la cantidad. La 
producción de Tarots, tanto en Estados Unidos como en diver-
sos países europeos –destacando entre ellos Italia–, no ha cesa-
do de aumentar, y la belleza y la originalidad de algunos de los 
nuevos diseños es admirable, muchos de ellos incluso rompien-
do con las rígidas teorías y los significados históricamente asig-
nados a las cartas. Al mismo tiempo, el hecho de que eruditos 
ampliamente reconocidos –como Mircea Eliade y sobre todo 
Carl Gustav Jung– se hayan ocupado con toda seriedad de los 
temas llamados «esotéricos», entre los que el Tarot ocupa un 
lugar especial, le ha conferido a éste una categoría de la que 
nunca antes –al menos en la historia actualmente conocida–

un poco de historia 
había disfrutado. Por otra parte, el interés del público en este 
instrumento de adivinación y autoconocimiento parece haberse 
disparado en los últimos años. A comienzos del siglo XXI, el 
Tarot es uno de los temas candentes de la llamada «nueva era» 
y las ventas de Tarots y de libros sobre él—que durante casi dos 
décadas habían languidecido— están experimentando un inusita­
do resurgir. Las páginas de internet dedicadas al Tarot son muy 
abundantes—tanto las informativas como las que ofrecen lecturas 
en línea— y la calidad de algunas de ellas, más que notable. Todo 
parece indicar que el presente siglo será el siglo del Tarot. 
31

Con el paso del tiempo, he descubierto que el Tarot es un instrumento de 
trabajo precioso, un guía seguro, prudente y sabio. He podido darme cuen-
ta de su poder y he visto que tras sus imágenes se puede descubrir a Dios.
Colette
El Tarot como instrumento 
de meditación y autoconocimiento
Físicamente el Tarot es sólo una serie de car-
tones con unos curiosos dibujos plasmados 
en ellos, pero resulta que esos dibujos son 
totalmente simbólicos. Podemos decir que el 
Tarot no habla otro lenguaje y no ofrece otros 
recursos que los simbólicos. El oculto signifi-
cado de sus emblemas se convierte en un 
alfabeto que admite combinaciones infinitas 
y en todas ellas tiene sentido. En los niveles
33

34
El Tarot Universal de Waite
más elevados llega a ofrecernos la clave de todos los misterios, 
la clave del mundo y la clave del alma humana y nos muestra 
una vía para conocernos a nosotros mismos. «El que se conoce 
a sí mismo, conoce a su Señor», decía un gran sabio sufi. En este 
sentido el Tarot es un poderoso instrumento de investigación 
mística y de autoconocimiento, cuyo valor difícilmente se podrá 
superar. Para Paul Foster Case la función más importante del 
Tarot es evocar pensamientos y potencialidades del alma huma-
na y cada una de sus cartas se corresponde con un aspecto de 
nuestro propio ser interno. De este modo, el hecho, de con-
centrarse sobre el Mago ayuda a desarrollar los poderes de 
concentración y atención, al hacerlo sobre la Sacerdotisa, se esti-
mula la memoria. La Emperatriz desarrolla la imaginación crea-
tiva, el Hierofante la intuición, y así sucesivamente. En su libro 
The Tarot, a Key to the Wisdom of the Ages,  recomienda reali-
zar una meditación diaria de cinco minutos de duración, miran-
do una de las cartas, sin pensar en nada, con la intención de que 
la contemplación de dicha figura evoque y ponga en marcha en 
nuestro subconsciente el poder o los poderes que se correspon-
den con ella. En este sentido –como decía Eliphas Lévi– alguien 
encerrado en una celda, sin nada más que una baraja del Tarot, 
podría acceder a todo el conocimiento del universo.
Una sencilla meditación de pocos minutos cada día sobre 
las cartas del Tarot, y especialmente sobre los Arcanos Mayores, 
puede producir resultados sorprendentes en nuestro desarrollo. 
Es conveniente realizarla siempre a la misma hora, en un lugar 
tranquilo donde no vayamos a ser interrumpidos ni molestados. 
También es aconsejable llevar un diario en el que anotemos tan-
to las ideas que surjan durante la propia meditación –y que 
deberán ser automáticamente sacadas de la mente para centrar 
a ésta de nuevo en la carta y nada más– como los sueños, los 
suesos relevantes ocurridos durante el día, las coincidencias y 
las ideas que surjan espontáneamente con una fuerza especial. 
Para quienes se interesen en profundizar en este tipo de estudio

35
El Loco:
El Mago:
La Sacerdotisa:
La Emperatriz:
El Emperador:
El Hierofante:
Los Amantes:
La Carroza:
La Fuerza:
El Ermitano:
La Rueda de la fortuna:
La Justicia:
El Ahorcado:
La Muerte:
La Templanza:
El Diablo:
La Torre:
La Estrella:
La Luna:
El Sol:
El Juicio:
El Mundo:
El principio creador.
Voluntad.
Inconsciente, unión.
Naturaleza, luz.
Construcción, orden.
La intuición.
División, momento de decidir.
Dominar las emociones.
El trabajo.
El Maestro interior.
Conciliación, aceptación.
Equilibrio.
Lo oculto, la renuncia.
Lo ilusorio.
La experiencia como base del 
conocimiento.
La renovación, el humor.
La transformación.
La meditación.
La consciencia corporal.
La fertilidad.
Lo eterno.
Realización, libertad.
y meditación sobre el Tarot, incluimos al final del libro los datos 
de BOTA.
Los siguientes atributos de los Arcanos Mayores pueden 
servir de guía para este tipo de meditación.

El Tarot Universal de Waite Un sen cill o e jer cici o Otra form a de utiliz are l Tarot cones taf in ali dad med it at iv aes ex tender los Arcano s May ores boca arriba en una mesa osu per-  fi cie plan a frente a no so tros, seg u ida men te real i zare mos cinco respiraci ones pro fund as, a qui eta ndol ue go la men te para ob ser var la scart as una a una, seguin vay an at ray endo nuestra a ten ci on, pro cur and ono pens aren nada pero eg i str ando las im-  genes que esp on tane a men tenos veng an. Tal vez nos centrem os en una carta oen una s po cas, no hay reglas para este e jer cici o,  lo important ees ob serva rl as con at enc ion, de jando que sea la vista la que selection e las que mas nos at rae ny que segu ida-  men te se pose en ellas cu anto tiempo des ee. Si surgen ideas, las anot are mos lu ego, enc as o contra rio de be mos record arque el lenguaje simb oli code lTa rot esta tr abaj ando sobre nuestra men te sub con sci en te, organ iz ando patron es y tal vez transmit i endo-  nos- s in pas arp or la men te conscient e- una part edel as abi-  dur i ay delos cono cimi en to s que susc read ores enc err a ron en esos extra nos di bu jos( aunque en real i dad, el proc eso ocurre jus-  tamente a la in versa: es nuestra men tesu b conscience la que,  est i mula dae in form a dap or el sim bol is mo del Tarot, real i za valios osa just es inter nos) . Nun case insist ira dem asia do en la import an cia de llevar un diario donde an to mes to do lore la-  cio nado cones to s ejerci cio s.  No hay que es per ar result a doses pectac ul are s. Pero s in duda al gun a los cambio s que ocurran en nuestra men tea niveles pro fund osse pl as mar an en nuestro comport a mien toyen nuestro ent or no: en el camino yl at rye ctor i aqu esiga nuestra vida. El sistema edu cat ivo actual, total men tec artes ian o, ha ol vi-  dado hace mucho tiempo que las en sen anza smas important es no entr an en no so trosa t raves dela men te conscient e. Hay much os maestros, pero po cos Maestros. Esta form a de trans mi-  tir in form aci on noes por sup u es to ex clu siva del Tarot. Hay seres human os que nos ense ian con su simple pre sen cia. Hay lugar es 36

Uso s del Tarot c uya in flue nci a es tambi end e este tipo y, por sup u es to, e saes la form a de ense nia r delos ver dade ros Maestros dela Human id ad,  eso s seres que no pore star fuera delal can ce de nuestros sent i dosf is cos son menos re ales.  En un in vel menos tr as c end en teel Tarot puede ser tam-  bien una her rami en tama muy util. Pore jem plo, ene s as oc as i ones en las que no so mos capaces de record arun no mb re- lo ten e-  mosen la punta del alen gua, como se sue lede cir- , una breve contempl aci on dela Sacer do tisa manten i endo la men teen blan co sue leb as tar para que lap al abra rebel de salga es ponta nea-  men teal a super fi cie de nuestra men te.  El Tarot como instrument o adi vina to rio La util i zac ion del Tarot como instrument o adi vina to rio es, al menos, tan anti gua como su uso para la med it aci on yel trabajo inter no y, por sup u es to, much om as fr ecu en tey popular. Des de los dias deE tte ill a has tal a epo ca actual, lap al abra Tarot no sue levo carene l hombre com unot racos aqu el as artes adivina tori as y to do lore lac ion a doc on ellas.  c Pero como fun c iona el Tarot? Co moe s posible que un as simple s fi gura s pint adas en un as pie z as de car tul in anos dig an el fu troo nos a consejo n sobre al go que no so tros cons cie n te no so mos capaces de aver i gura?  Mas all a del a men tec on s cie n te, que es la que us ted esta util i zandop a rale erest as line as yl aqu e todos usa mos habitual-  men teen nuestro s que h acer es diario s, hay una parted e no so-  tros mis mos dela cu al nonos solem os per catar, y que se ha dado en llamar men tesu b conscience. Seguin afi r man dist in t as corri en tes filos of ic as des de hace cie n tose in clu so miles de a no s,  esa part ede no so tros los a be to do, lo cono cet odo y por lot an-  to lo puede pre dec ir to do. El tiempo ye l ESPa cio no tien en sobre 37

El Tarot Universal de Waite 
38 
ella el mismo rígido dominio que ejercen sobre nuestro cuerpo o 
sobre nuestra mente consciente. Según el psicólogo suizo Carl 
Gustav Jung, la mente subconsciente está en contacto perma­
nente con el subconsciente colectivo: un vasto depósito donde 
se acumulan todos los conocimientos, toda la sabiduría y todas 
las experiencias de la humanidad, desde los primeros poblado­
res de esta tierra hasta nuestros días. 
Cualquiera que haya sido su origen, las figuras del Tarot 
parece que fueron ideadas de acuerdo a ciertos patrones de esa 
mente subconsciente: ello explicaría por qué son tan eficaces 
para sacar a la superficie y traer a la consciencia conocimientos 
a los que usualmente no tenemos acceso, pues los seres huma­
nos hemos sido construidos de forma que entre la mente cons­
ciente y la subconsciente existe una barrera bastante difícil de 
franquear y el tipo de vida occidental, totalmente volcado hacia 
el exterior y que desprecia las tenues señales que usualmente 
nos llegan del lado subconsciente (en forma de sueños, premo­
niciones, intuiciones, señales, etc.), no ha hecho sino reforzar 
infinitamente dicha barrera. 
Pero el hecho es que esos conocimientos subconscientes 
están ahí, muchas veces diríase que Pujando por salir, tan sólo a 
la espera de que aquietemos la mente consciente, nos aparte­
mos por un momento del mundanal ruido y miremos, aunque 
sea tímidamente, hacia nuestro interior. Y el Tarot es un instru­
mento muy útil para facilitar el afloramiento de dichos conoci­
mientos. Así, parece que la mente subconsciente influye sin dar­
nos cuenta en los movimientos de balarjar, cortar y escoger las 
cartas, de modo que al ser éstas descubiertas tengan una rela­
ción muy directa con el asunto que se quiere consultar. El tipo de 
conocimiento que el Tarot nos traerá del subconsciente somos 
nosotros quienes lo decidimos. De ahí su uso meditativo, de 
desarrollo o adivinatorio. 
¿Qué se puede preguntar? Cualquier cosa, pero el tipo de 
pregunta que uno haga es muy importante para determinar la

Uso s del Tarot resp u esta que el Tarot nos dar a. La pre c is ion dela resp u esta esta en fun ci on dela exact it ud dela pre gun ta. Cu an to mas pre c is a sea la pre gun ta, mas pre c is as era la resp u esta. S is up re gun tae s v aga y general la resp u esta tambi en lo sera; sila pre gun tia tien e much os de tall es, esp ere una resp u esta muy de tall ada.  Por sup u est o, tambi ene s important e que en el moment o en que formule la pre gun t as u men tees tec entr ada. Sies tae ner vio so y an sio so, aunque es to s sent i mien to s not eng an nada que verco n la pre gun ta, las cart as del Tarot le dar an una resp u esta sobre salta day err a tica, que sera di fic il interpret ar. Es bu eno ten er la men tet ran qu ill a. Pero tam poco esn ees a rio h acer yoga o med it arantes de h acer una pre gun tia un que por sup u est o no le haria ning u nda no! ) . To do lo que tien e que h acer es de jar a un lado sus pre o cup aci ones durante un moment o, cal marla men te, ob serva r tranquil a men tel as rip racion s in pens aren nada. y lu ego pre gun tar.  Es nec esario dec irl que la cree nci a en el Tarot es un com-  pone n tees en cia l del proc eso. Uno de be cree n so solo que el Tarot le puede responder, sino que lo hara. S in esta cree nci a,  to does in util. Si eso tr a person a qui en le lee l Tarot, tambi en de ber a al menos consider are l consejo que esta person a led e, y node se chars usp a labra sco mos if u er an los des var ios de un loco. El Tarot solo fun c iona para a quell os que des e an escu char.  Si uno no qui ere que lo ayu den, no hay man era de que el Tarot loh a ga. La fee act u a como un puente entre different es niveles del ser, entre diferent es niveles dela exist en cia, y pore se pun te puede circular la en erg i a( lo mismo occur een ciertos tipo s de cu racion oen much os actos religios os) . S in fe no hay puente y nose puede rec i bir nada.  Siusted qui ere ques ele ayu de, y cree que puede ob ten er una resp u esta, esta list o para h acer una pre gun ta.  Hay tambi eno cations en las que, a primera vista, uno pod ria pens arque la resp u esta que el Tarot nos dano guard a rel aci on al gun a con la pre gun taque hemos he ch on ni conn u est ra 39

El Tarot Universal de Waite 
situación actual. En estos casos no debemos precipitarnos en 
hacer este tipo de juicios. Vale la pena concedernos un tiempo 
para reflexionar sobre la respuesta que las cartas nos han dado, 
así como sobre nuestra pregunta. En algún momento la res-
puesta se hará clara en nuestra mente. 
Lea cuidadosamente los significados de cada carta según 
se explican a continuación, teniendo en cuenta que éstas son 
sólo algunas ideas iniciales, que le ayudarán a empezar a cons-
truir una relación con el Tarot que tiene que ser única y personal. 
Si alguna de las ideas o de los significados atribuidos a una car-
ta que usted lea en este libro o en cualquier otro le parecen ina-
decuados, deséchelos sin más y aplique los suyos en su lugar. 
Reflexione sobre las descripciones dadas y deténgase un 
momento a pensar qué le dice a usted cada una de las cartas, 
pues, de nuevo, la información que aquí damos no pretende ser 
sino una guía que lo inicie y lo estimule a realizar sus propios 
descubrimientos. 
40

Los Arcanos May ores Las 22 cart as que com pone n los Arcano s May ores, o tri un fo s, conti en en el sign if ica do y los mister ios mas prof undos. Cad a uno delos 22 Arcano s May ores ref le j a un aspect ode nuestro prop ios er, un aspect ode lae ner gia que form a el mundo en el cu a lest amos in mer sos e in clu so un aspect ode la Div in i dad. Eno tro orden decos as, los 22 Arcano s May ores represent an una pro gres ion, nos mu estr an el paso del alma human a pore l mundo, vida tr as vida, en su camino as c en-  dent ehaci a la comp ren sion, haci a el cono ci-  mien to y lap er fec ci on.  41

42
El Tarot Universal de Waite
Sin duda las 22 cartas que forman los Arcanos Mayores 
son la parte más importante del Tarot, sin ellas, no sería otra 
cosa que una baraja de cartas. Quién sabe cuál sea realmente su 
significado y si algún día se llegue a descubrir totalmente. Es 
posible que ese significado jamás nos pueda llegar de una fuen-
te externa y debamos buscarlo en nuestro interior. De hecho, 
algunas escuelas limitaron su estudio del Tarot a estos 22 
Arcanos Mayores.
Los siguientes comentarios sobre los Arcanos Mayores son 
sólo una guía inicial, una sencilla indicación que sirva al estu-
diante como punto de partida para sus propias averiguaciones y 
experiencias.

Los Arcano s May ores 0 ELLO CO El Loco: El esp i rita S in el concept o del Cero, nuestro sistema mate mati co note nd ria sent ido. Del mis momo do, el Loco es una parte es enc i al del Tarot, por que es la chis p aqu eh ace que to do lo dem asse mu e va, ese el spirit u, el alien to divino queda vida e in spira el primer paso haci a la real i zac ion yl a consumaci on. Aunque a menu do el primer paso e nun tray ect ola rg opare cepe que rio, i ese primer paso es vital por que s in leno habr a via je! El Loco es lac a usa sub yace n tetra st odo sloes fec to s, el p oder o culto tr as to das las manifest aci ones yl a sem ill adel fin sem brad a en to do principi o.  Es la nada delac u al surge to do.  43

El Tarot Universal de Waite 
El Loco es potencial sin moldear, puro e inocente, ni posi-
tivo ni negativo, aunque contiene la posibilidad de ambos. Es el 
alma incondicional a punto de manifestarse por primera vez 
para empezar a aprender las lecciones del mundo. A pesar de 
que todos lo llaman Loco, él no les presta atención, y simple-
mente sigue su camino. Sin duda lo que le dicen puede estar jus-
tificado, ya que su ignorancia sobre el mundo lo puede llevar a 
hacer cosas que personas con más experiencia nunca imagi-
narían. Pero en estas cosas, puede él hallar conocimiento y 
esclarecimiento. No se preocupa por lo que los demás piensan o 
dicen sobre él, porque sabe que lo que hace es bueno para él. 
Su enfoque sobre la vida es raro y poco convencional, ya 
que hace lo que le resulta cómodo. Para muchos el punto de vis-
ta del Loco puede ser extravagante, escandalizador e incluso 
alarmante. Pero es todo lo que el Loco sabe, y dado que la üni-
ca aprobación que necesita es la suya, continuará con su vida, 
a pesar de lo que todos los demás piensen de él. Tiene una fe 
total en sí mismo. Tal vez no tenga nada de loco. 
El Loco no se esconde a sí mismo de la luz, porque él es la 
luz, la luz maravillosa que brilla en cada niño antes de ver el 
mundo y ser forzado a construir paredes y barreras para prote-
gerse. Con esta inocencia viene la confianza total y audaz en 
otros, y la total confianza en uno mismo que le permite ver el 
mundo con nuevos ojos y aprender cosas cada día de su vida. 
iPiense en cómo mejoraría el mundo si todos actuaran de esa 
manera! Lástima que sólo los niños, y el Loco, vean esa luz. 
El Loco suele representar inicios, experiencias y opciones 
nuevas; los primeros pasos de un nuevo camino y las primeras 
palabras escritas en una página en blanco. Como los Ases de los 
Arcanos Menores, esos inicios no son ni positivos ni negativos, 
pero tienen el potencial de volverse cualquiera de los dos, según 
las decisiones que usted tome y el camino que siga. Pero esto no 
debe preocuparle, porque cuando se inicia un viaje nadie sabe 
qué pasará en el camino. Nunca permita que otra persona 
44

Los Arcanos Mayores 
controle su vida. Viva el presente y confie en sus capacidades, 
como lo hace el Loco. 
Esos viajes siempre implican un cierto riesgo, por eso al 
Loco se le representa caminando hacia la orilla de un alto risco. 
Como en todas las experiencias nuevas existe el riesgo de fallar 
y también la certeza de un cambio; el grado de ese cambio y 
cómo aparecerá es lo que no sabemos. El Loco no tiene temo-
res a la hora de tomar riesgos, ¿por qué usted sí? A través de los 
primeros pasos es como aprendemos a caminar, y por medio de 
los cambios aprendemos a vivir en armonía y paz. Láncese al 
abismo de lo desconocido y sepa que, aun si eventualmente 
cae, pronto se levantará. 
Significado: 
Decisión importante. La persona se halla ante 
una elección que debe decidir con cuidado pero 
también con coraje y, sobre todo, atendiendo a 
su intuición y sus corazonadas. Se pueden 
tomar riesgos. 
Invertida: 
Hay peligro de que se escoja mal. Es aconsejable 
actuar con la máxima precaución y prudencia. 
45

Los Arcanos Mayores: EL MAGO
El Mago: La Voluntad
El Mago es el número Uno, el número de la creación y de la individualidad; su poder radica en la transformación a través de la voluntad. El Mago puede tomar la nada de la que surgió El Loco y darle forma, haciendo uno de cero. Sin duda, este es un poder divino, y en realidad, el Mago actúa como un conductor de un poder superior que domina todo el mundo material.
Dado que lo único que podemos observar en el mundo físico es el resultado de este proceso, a menudo los actos que realiza el Mago nos parecen mágicos. El nombre "El Mago" puede sonar extraño para alguien con un poder tan real, ya que la palabra evoca la imagen de un ilusionista, cuyo único poder es la habilidad manual y la

El Tarot Universal de Waite 
desorientación. Sin embargo, en muchos aspectos el Mago es 
también similar al ilusionista. Él está seguro de su destreza y de su 
habilidad para producir los efectos que desea. Su poder real pro-
viene de fuerzas externas a él y no tiene poder sin estas fuentes, 
pues depende de quien está «tras el escenario», al igual que el illu-
sionista. No obstante, tanto el mago como el Mago son igual de 
importantes para sus poderes como sus poderes lo son para ellos. 
Sin un conducto, el poder en sí mismo es impotente e inútil. 
Con sus poderes el Mago tiene influencia sobre todo: teoría 
y práctica, lógica y emoción, pensamiento y acción. El símbolo 
del infinito indica su poder ilimitado, que le viene de fuentes 
externas, pero está bajo su control. Y mientras el Mago recuer-
de que posee este poder, aunque pierda toda su habilidad terre-
nal, no podrá llamarse impotente. Pues su Voluntad es un po-
der que, aunque puede ser sometido, nunca podrá ser destruido. 
Otra asociación casi universal con el Mago es el esquema 
rojo y blanco. Este tema se repite en todo el Tarot y es muy 
simbólico que empiece con esta carta y no con el Loco. Mientras 
que el Loco era el potencial, la posibilidad de lo positivo y de lo 
negativo, el Mago es la unión de lo positivo y lo negativo. Él 
crea y conserva; destruye y redime. Su verdadero poder es que 
no sólo sabe lo que debe hacer, sino que sabe cómo hacerlo y 
por qué. Y lo hace. El Mago nos recuerda que sólo desear no 
cambiará nada, pero una decisión puede cambiarlo todo. El 
deseo de crear no es nada sin la habilidad de crear, y viceversa. 
Cuando aparece el Mago, ello indica que usted está listo 
para convertirse en conducto del poder, como él lo es. Las fuer-
zas de la creación y de la destrucción siempre han estado bajo su 
dominio, pero ahora usted tiene la sabiduría y la confianza nece-
sarias para usarlas de manera constructiva. Ahora es el momen-
to de actuar, si usted sabe lo que quiere lograr y por qué. Dado 
que los poderes de transformación están bajo su dominio, con-
vierta sus deseos en objetivos, sus pensamientos en acciones, 
sus metas en logros. Si recientemente ha fracasado, ahora puede 
48

Los Arcanos Mayores 
convertir ese fracaso en éxito, tan fácil como el Mago transforma 
el fuego en agua. Los únicos límites que tiene son los que usted 
mismo se imponga. 
Las manifestaciones externas de ese poder son tan nume­
rosas como diferentes, pero el efecto exterior más común de la 
influencia del Mago es el no poder ser influenciado y la confian­
za total. Darse cuenta de que el mundo está bajo su control es lo 
que inspira este tipo de confianza. Salga al mundo, fije su men­
te en la meta en la que está interesado y luego dé un paso atrás 
y observe, mientras todo cae en su lugar, bajo su control. Por 
último, el mensaje del Mago es sencillo a pesar de su poder com­
plejo, ilimitado e infinito. Su vida está bajo su control. Su vida es 
lo que usted quiere que sea. Su vida es como usted la hace. 
Significado: 
Voluntad, dominio, capacidad de organización, 
talento creativo. La capacidad de tomar el 
poder de arriba y dirigirlo hacia abajo, hacia la 
manifestación, con resultados positivos. 
Invertida: 
Indecisión, incapacidad, ineptitud, bloqueo de 
las energías creativas, miedo a experimentar y a 
probar cosas nuevas, uso del poder con fines 
destructivos. 
49

Los Arcanos Mayores 
2 
LA SACERDOTISA 
La Sacerdotisa: La sabiduría oculta 
Se dice que, de todos los Arcanos Mayores, la Sacerdotisa es el 
más difícil de calificar sólo con palabras, ya que mucho de su 
poder y de su habilidad está cubierto por el velo del misterio y 
es difícil que alguien lo comprenda totalmente. Cada carta del 
Tarot le dice algo diferente a cada uno, pero la Sacerdotisa es la 
que permite un rango de interpretaciones más amplio, porque 
habla directamente a la Voz Interna, a nuestro inconsciente. Ella 
es la manifestación del inconsciente y del misterio, en nuestro 
mundo cotidiano. Con frecuencia, el hecho de tratar de ver 
cómo funcionan esos misterios destruye su propósito, y la Gran 
51

El Tarot Universal de Waite 
Sacerdotisa se debe explicar con todo detalle posible, pero 
teniendo esto en mente. 
La Sacerdotisa es, sobre todo, la base de donde surge el 
poder manejado por el Mago. Ella es el potencial limitado que 
le permite a él transformar y crear lo que desea su Voluntad. La 
clave para descubrir algunos de los misterios de la Sacerdotisa es 
entender este tipo de equilibrio, como el equilibrio entre el 
potencial y la creación, entre lo masculino y lo femenino. En 
lugar de integrar a los opuestos, la Sacerdotisa los mantiene 
separados y no obstante en equilibrio. Ella es la balanza en sí 
misma; este simbolismo se encuentra en muchas barajas del 
Tarot. No puede haber poder sin este equilibrio. 
El segundo motivo simbólico que se encuentra en casi 
todas las representaciones de la Gran Sacerdotisa son los sím-
bolos del inconsciente. En el Tarot universal de Waite este moti-
vo es especialmente notable, pero en la mayoría de las barajas 
figura al menos una imagen lunar, que como sabemos está vin-
culada al inconsciente. La mayoría de los Tarots que incluyen la 
simbología de los pilares gemelos también representan un velo 
extendido entre ambos pilares; la Gran Sacerdotisa está entre 
nosotros y ese velo, como moderadora. Detrás del velo se 
encuentran los poderes del inconsciente, que no podemos 
entender pero que, a través de ella, podemos aprender a con-
trolar. Ella es la puerta de acceso hacia reinos que nunca com-
prenderemos ni dominaremos por completo. 
Aunque para cualquiera sería imposible aprender todos los 
misterios y los secretos de la Gran Sacerdotisa, ella sigue siendo 
una guía para los que deseamos aventurarnos en las profundi-
dades de nuestra mente, a fin de descubrir los verdaderos pode-
res escondidos en lo más profundo de nosotros. Éste es el mis-
mo poder que se representa en el Mago, pero el alcance del 
poder de la Sacerdotisa es muy diferente. Mientras que el Mago 
enfoca sus poderes al exterior, para conseguir un efecto significa-
tivo en el mundo, la Gran Sacerdotisa nos muestra que también 
52

Los Arcanos Mayores 
podemos usar estos poderes en un nivel interior, para enrique-
cernos y transformarnos a nosotros mismos. Sin duda, esas 
transformaciones no son tan espectaculares como las del Mago, 
pero casi siempre son más poderosas. 
La Gran Sacerdotisa representa los misterios del incons-
ciente y de la Voz Interior, y con frecuencia su aspecto es una 
señal de que nuestra propia intuición trata de enviarnos un men-
saje. A menudo el inconsciente nos habla con símbolos, así que 
vigile su alrededor en busca de cualquier cosa que parezca fue-
ra de lo común. Dicho esto, si tiene que tomar una decisión 
importante, cuando aparece la Sacerdotisa ello suele indicar 
que, si es usted paciente y está abierto a los susurros que le lle-
gan desde el interior, se le revelarán las respuestas. Sólo tiene 
que esperar y recibir los mensajes. La enseñanza de la Gran 
Sacerdotisa es que todo lo que usted necesita saber ya existe en 
su interior. 
Al hablar de la Sacerdotisa tampoco se puede evitar el 
tema de la dualidad. Con frecuencia este arcano es un signo de 
la sombra, de la parte negativa de nuestra personalidad, que 
nadie ve, y de la que usted mismo puede no ser consciente. (En 
este sentido, el término «negativo» no se refiere al mal, sólo es el 
polo opuesto de la parte positiva y expresiva de nuestra perso-
nalidad.) Si usted acepta esa sombra que hay en su interior, los 
poderes de la Sacerdotisa se abrirán a usted, si es que desea 
usarlos. En la mayoría de las personas el lado de la Sombra 
representa la pasividad, por lo tanto la Sacerdotisa puede abo-
gar por la necesidad de mantenerse pasivo en alguna situación 
dada. No siempre es necesario actuar, a veces los objetivos se 
logran mejor a través de la inactividad. 
Significado: 
El futuro desconocido. Las influencias ocultas. 
De especial significación para todo tipo de artis-
tas. Para un hombre puede también representar 
a la mujer ideal, perfecta. En una mujer puede 
53

54
El Tarot Universal de Waite
indicar la posibilidad de poseer ella misma esas 
virtudes.
Invertida:	
Goce sensual. Engaño. Conocimiento superfi-
cial. Indicación de que estamos ignorando los 
impulsos que nos llegan desde el interior, tal vez 
nos indica que estamos buscando una confirma-
ción externa a todo, antes de comprometernos.

Los Arcano s May ores 3 LA EMPER ATRI Z La Em per atriz: La a cci on fru c if era La Em per atriz represent a la cul mina cio ndel a filos of i adua lista delos tres primer os Arcano s May ores, as f como del as ense nan-  za ses pir it u ales de estas tres cart as. A hora el Tarot emp i eza at ra tar con la uni fic aci on del esp i ritu, masque co nuna dico to mia simple de positiv oy nega t ivo, de men tey cue rpo. La Em per atriz es lau it i map arte de esta tria da, y represent a el cue rpo f is i coy el mundo material. De ella pro vie netodo el placer delos sent ido s y la abundancia dela vida en to das su sforms. Tambi ene sel ar que tipo dela madre, yatr aves de ella ten emo sun primer vis-  lu mb rede l p oder del amor en el Tarot.  55

El Tarot Universal de Waite
56
El mundo de la Emperatriz es el lugar perfecto, hermoso, 
ideal, totalmente natural, sin colores, luces ni sonidos artificiales. 
Es un lugar de generosidad y fertilidad, una representación viva 
del proceso de creación y nacimiento que la Emperatriz misma 
simboliza. Ella no sólo vive en ese lugar, sino que es el lugar, así 
como la Sacerdotisa es el equilibrio que mantiene apartado lo 
positivo de lo negativo. La Emperatriz no es menos bella que las 
flores que esparcen su aroma en los campos, no es menos fértil 
que el suelo que está debajo de su trono. Si algo representa la 
idea de la Madre Tierra en el Tarot es la Emperatriz.
Su poder principal, al igual que en los dos arcanos anterio-
res, es el poder de la creación. Pero su creación no se basa en el 
mundo en el que ella desea vivir, o en la persona que desea ser, 
porque ella tiene ese mundo y es esa persona. Ella crea la vida 
en sus formas infinitas. La Emperatriz es el arquetipo de la 
madre, la creadora máxima y la dadora de vida, así sus relacio-
nes pueden extenderse más allá de la creatividad a la fertilidad, 
el embarazo y la intimidante tarea de la maternidad, a la que 
siempre se enfrenta con una sonrisa y con alegría. A ella le com-
placen todas las cosas, en particular sus propias creaciones y 
todo en la naturaleza es creación suya.
La Emperatriz también representa la idea del amor incon-
dicional, que está unida al tema de la maternidad. Ella no pide, 
no pone condiciones, ama a todo por igual y con todo el poder 
que puede. Puede decirse que de esto se deriva su única debili-
dad real, y es algo con lo que todas las madres se enfrentan en 
algún momento. A menudo es demasiado protectora con sus 
creaciones, y no desea ningún daño para ellas. Esto interrum-
piría la dicha y la felicidad eterna de su reino. Pero, tal como 
está, el reino de la Emperatriz es la representación tanto de la be-
lleza como de la inactividad. Así que, mientras el amor de la 
Emperatriz puede hacer sentirse tan seguro como en los brazos 
de una madre, también puede volverse una prisión, si dura 
mucho tiempo.

Los Arcanos Mayores
Cuando la Emperatriz aparece en su vida, debe hacer un
esfuerzo especial para abrirse a su amor perfecto e incondicio-
nal. De esa manera puede parecerse más a ella: amable y afec-
tiva, graciosa y elegante. A menudo estas cualidades se descui-
dan, pero también son útiles en un mundo duro y apático. Así,
en lugar de caminar pausada y pesadamente por la vida, iconcé-
dase el tiempo para celebrarla! Con frecuencia la Emperatriz
puede presagiar la concepción o el nacimiento de un niño, y en
esa circunstancia hay una razón aún mayor que celebrar. Inspire
a otros para que hagan lo mismo; la Emperatriz es líder, y el
poder que ejerce sobre otras personas es firme, pero amoroso.
Conozca esto y conduzcase como lo haría ella.
Sepa también que usted siempre es libre de disfrutar el
amor perfecto y abundante de la Emperatriz. Aun si sabe que
luego tendrá que volver al «mundo real», en realidad le agra-
darían unas vacaciones de la vida agitada y artificial que la
mayoría vivimos en estos días. Pase algún tiempo en el exterior,
al aire libre, disfrutando todos los aspectos de la creación. Y lue-
go, cuando regrese a donde estaba, el poder y la belleza crea-
dora de la Emperatriz continuarán inspirándolo y dándole fuer-
za. Fortalezca su conexión innata con la creatividad de la Tierra
y, por asociación, fortalezca su propio poder creativo. Cultive su
creatividad y sembrará las semillas que le darán una cosecha
generosa.
Significado:
Creatividad, productividad, embarazo, materni-
dad, abundancia, buenas cosechas, éxito y un
entorno seguro y exento de peligros. Fertilidad,
tanto mental como física.
Invertida:
Inactividad, destrucción, pérdida de cosechas,
enfermedad física o mental, pobreza, problemas
en un embarazo. Actividad estéril.
57

59
Los Arcanos Mayores
El Emperador: Liderazgo, autoridad y control
El Emperador representa el poder de la mente para darle forma 
al mundo. Esta acción no se realiza por el deseo, sino a través de 
la palabra hablada o escrita. El Emperador es la representación 
–y el gobernador– del mundo estructurado y reglamentado. Éste 
es un mundo ideal como el de la Emperatriz, aunque no siempre 
tan bello o generoso. Pero sólo por ser más duro no significa que 
no tenga lo necesario para la iluminación; por el contrario, es 
imprescindible para equilibrar mente y cuerpo, varón y mujer.
El Emperador es lo contrario de la Emperatriz en muchos 
aspectos. Ella es la Madre, él es el arquetipo del Padre, sabio en 
el conocimiento del mundo y poseyendo toda la información

60
El Tarot Universal de Waite
sobre cómo vivir junto a los demás como parte de una estructu-
ra. El Emperador posee un corazón fuerte y poderoso, como 
todo padre debería tener, pero muestra este lado de sí mismo a 
través de la imposición de lineamientos y reglas estrictas, como 
la mayoría de los padres. Se podría decir que es aún más pro-
tector que la Emperatriz, pues él ha creado el orden en el caos y 
no desea que nada perturbe ese orden. Bajo sus ropajes reales 
se esconde la armadura, que usa con orgullo cuando defiende a 
aquellos que están bajo su protección.
El Emperador nos enseña muchas cosas, la primera es que 
toda regla tiene un motivo y una razón de ser. Si podemos 
entender esto, tal vez este mundo no nos parezca tan limitante. 
De hecho, todas las restricciones son por nuestro propio bien, 
porque sin la ley y el orden que esta carta simboliza de manera 
tan poderosa, el mundo caería en la anarquía y el caos. Tanto el 
gobierno como la ley extraen de ella su poder, pero a diferencia 
de las figuras de gobierno en los tiempos modernos, el Empe-
rador no puede corromperse por el poder. Es, en realidad, el 
amo de su reino, y lo gobierno con mano firme pero justa. 
Escuchará el consejo de otros, aunque la decisión final siempre 
la tomará él. La guerra es una de sus muchas herramientas y no 
vacilará en usar la violencia para proteger a aquellos que le inte-
resan. Los privilegiados a los que protege siempre le responden 
con la lealtad y el respeto que se merece. Pero el poder del 
Emperador no se extiende sólo al control político. También es el 
padre, el modelo del papel masculino que aconseja, guía y da 
seguridad. Toma lo que él aprendió y lo pasa a la siguiente gene-
ración, para que algún día otros puedan ser tan sabios y pode-
rosos como lo es él.
En la interpretación, cualquiera de los Arcanos Mayores 
puede representar a personas, pero el Emperador es el tipo de 
energía que más a menudo se manifiesta en la forma de una 
persona. Es evidente que todo tipo de líderes y padres tienen 
algo de su influencia, pero también puede mostrar a alguien que

Los Arcanos Mayores 
actúa como padre al ordenar y estructurar. Es una fuerza regu­
ladora y así se asocia con el gobierno, la burocracia y el sistema 
legal; su aparición suele indicar el encuentro con uno o más de 
estos sistemas. El Emperador también puede personificar la 
usurpación del poder y el control, por uno mismo o por alguien 
cercano. Si es usted la persona que está en el poder, deberá 
tener cuidado de usarlo siempre con sabiduría. 
Sobre todo, el Emperador muestra los beneficios de la 
estructura y la lógica, que gobierna sobre las emociones y los 
deseos más bajos. A menudo, no se desea que la mente domine 
al corazón, pero en algunos casos es necesario e incluso agra­
dable. Cuando se tiene que hacer una elección difícil es impor­
tante mantener la concentración y el enfoque, y esto es algo que 
la fuerza del Emperador nos permite lograr. Disfrute la confian­
za que él da. Avance con ímpetu y firmeza y haga lo que sabe 
que es mejor. Si puede dominarse, tendrá pocos problemas para 
dominar al mundo y a todas las cosas que hay en él. 
Significado: 
Liderazgo, actividad mental, dominación, domi­
nio, paternidad. Dictadura. Pasión, pero siem­
pre controlada por la inteligencia. 
Invertida: 
Inmadurez, dependencia emocional o esclavi­
tud de las figuras de autoridad, ya se trate de los 
padres o de otras personas. Posibilidad de ser 
defraudado en herencias. Enfoque excesiva­
mente estrecho, falta de iniciativa. La persona 
es hombre por fuera, niño por dentro. 
61

Los Arcano s May ores 5 EL HIER OF ANTE El Hie rof ante: La or to do xia con ven c ional El Hie rof an tees elar que tipo del mundo espiri tu al. Esta es la carta del as cree nci as, tanto religios as como de ot rot ipo, aunque ti ende a en foca r seen los aspect os religios os y espiri tu ales, ya que el propio Hie rof ante es a men udo represent a do como un hombre santo. Enal gun osT a rots a esta carta sela cono ce como el Papa o el Sumo Sacer do te. Pero en real i dad, el Hie rof an tees la person a que tien e cono cimi en to s《 pro hi bid os》 o《 secret os》 .  Aunque est ose aplica con fac ili dad a los cl eri go s, su al can cees mucho mayor. Deal gun a man era sep uede dec ir que cad a hom-  bre y cad a mujer e sun Hie rof ante.  63

El Tarot Universal de Waite 
El Hierofante puede simbolizar a un grupo o a más de una 
persona, y en la mayoría de los casos está mejor representado 
por una institución más que por una sola persona, pues su poder 
es el del grupo y de la sociedad que cambia al mundo. En esta 
quinta repetición continúa el mismo tema del control y el cambio 
que apareció primero con el Mago; todavía existe un líder bien 
definido, pero las personas no lo siguen porque se les ordene. Lo 
siguen porque son parte del grupo. Las principales filosofías del 
Hierofante son que no hay un «yo» en el «equipo», y que el bie-
nestar de muchos es más importante que el bienestar de uno. 
Tal filosofía puede parecer innecesariamente restrictiva 
pero, como el Emperador nos enseñó, la restricción conduce al 
orden. El Hierofante está encargado de mantener y propagar la 
tradición y las creencias convencionales, y esquiva a cualquiera 
que vaya en contra de estas creencias. Los objetivos del 
Hierofante son el equilibrio y la conformidad, y no hace énfasis 
en lo positivo ni lo negativo, lo único que importa es la enseñan-
za, la tradición. En casos extremos, esto puede tener efectos 
negativos, pero en la mayoría de las ocasiones es bueno tener 
unas tradiciones que seguir. Ejemplos excelentes de esto son las 
tradiciones y las ceremonias de la Iglesia, claramente represen-
tadas en esta carta. 
En un nivel más personal, el Hierofante también es un 
maestro. Una función importante de todo líder espiritual es ini-
ciar a otros y enseñarles las costumbres del grupo. Es obvio que 
aquel que guarda el secreto y al que se le confían las tradiciones 
del grupo es el candidato principal para enseñárselas a otros, y 
el Hierofante realiza bien esta función. Aunque su enfoque de la 
enseñanza parece ser convencional, y por el momento evita las 
expresiones individuales, esto puede ser útil. Hasta que el alum-
no no domine las costumbres del grupo, no podrá tomar una 
decisión adecuada sobre si permanecer en él o dejarlo. 
Cuando aparece el Hierofante suele hacerlo en forma de 
un maestro, que nos instruye en las tradiciones de sus creencias 
64

65
Los Arcanos Mayores
particulares. Estos maestros no siempre tienen antecedentes 
espirituales o místicos; un patrón que entrena a un empleado 
nuevo en el funcionamiento de un negocio es tan Hierofante 
como cualquier maestro espiritual o religioso. Si en su situación 
actual parece necesitar más experiencia, puede usted hacer una 
llamada interior, puede estar abierto a la presencia de un maes-
tro en su vida. Pero no cometa el grave error de buscar de mane-
ra abierta a ese maestro. Como dice el viejo proverbio, cuando 
el alumno está preparado, el maestro aparece.
El Hierofante también puede representar actividades y 
creencias de grupos y, en cualquier caso, acentúa el apoyo a las 
instituciones y el respeto por las reglas. Por eso, si planea reali-
zar algo revolucionario, la repetida aparición del Hierofante es 
una buena señal de que, por el momento, debe olvidarse de esa 
acción y seguir la corriente. La manera tradicional de hacer las 
cosas debe funcionar la mayoría de las veces, ide lo contrario no 
habría durado lo suficiente como para llegar a ser una tradición! 
Sin embargo, cuando se prueba que una idea está equivocada 
sin duda es tiempo de cambiar. El verdadero Hierofante es el 
que siente un respeto profundo por sus creencias, pero no las 
seguiría ciegamente hasta buscar su propia ruina. Es la enseñan-
za externa, así como la Sacerdotisa representa a la enseñanza 
secreta, que se imparte sólo a los iniciados.
Significado:	 Ortodoxia. Apego a las formas externas, a lo 
convencional, al credo y al ritual. Tradiciona-
lismo. Necesidad de seguir las normas social-
mente aceptadas.
Invertida:	 Rompimiento con lo convencional. Mente 
abierta, dispuesta a aceptar nuevas ideas y nue-
vas formas de pensamiento.

Los Arcanos Mayores 
6 
LOS AMANTES 
Los Amantes: El amor, la armonía 
La carta de los Amantes no habla sólo de amor y sexualidad, ya 
que tiene varios significados, todos relacionados con la dualidad. 
El concepto de los Amantes es un poderoso símbolo de la unión 
armoniosa de dos seres, pero también representa la necesidad de 
una elección adecuada, y algunos conceptos interesantes sobre la 
relación de nuestras mentes conscientes con el poder que une a 
estos amantes. En nuestra cultura, que tiene muchas palabras y 
definiciones para la emoción del amor, es normal que la imagen 
del amor expresada en el Tarot tenga muchos significados. 
Los Amantes son principalmente una carta de emociones 
y, con frecuencia, representa un amor con bendición divina, ya 
67

68
El Tarot Universal de Waite
sea de Cupido, de un ángel o del propio Dios. Esto parece impli-
car que sólo algo bueno puede venir de esta unión, aunque con 
esta carta dualista siempre existe la posibilidad de un final triste, 
a pesar del mejor de los inicios. Después de todo, el amor es 
como un fuego que puede encender la llama de la pasión, pero 
también puede consumir y destruir si se usa sin precaución. El 
amor es algo maravilloso, pero el amor profano o no correspon-
dido tiene el poder de dañar a familias y a personas. Los 
Amantes tienen dentro de ellos la posibilidad de ese amor y 
siempre debemos tener cuidado con esto.
El elemento que rige a los Amantes es el aire y por lo tan-
to debemos esperar que la mayoría de los significados se rela-
cionen con el espíritu y la mente. En esta carta se representa por 
primera vez el concepto de elección entre lo positivo y lo nega-
tivo, representado en muchos Tarots con la antigua simbología 
de un hombre decidiendo entre dos amantes. Esta encrucijada 
moral es también planteada por la carta de los Amantes, y nos 
dice que consideremos todas las consecuencias antes de actuar. 
La situación puede ser tan sencilla como una bifurcación en el 
camino, con dos senderos para elegir, o una decisión más com-
plicada en la que nuestras creencias e ideales más firmes tengan 
que ser puestos a prueba. Es evidente que en los momentos de 
la difícil elección necesitamos un guía superior.
Pero tal vez el significado más importante de los Amantes 
sea el representado en el Tarot universal de Waite. Esta imagen 
muestra al hombre mirando a la mujer, que a su vez mira a la 
figura divina que está sobre ellos. El hombre no puede ver al 
ángel y debe confiar en que la mujer lo verá por él. De igual for-
ma, la mente consciente (el hombre) no tiene acceso directo a 
los Poderes Superiores (el ángel). El inconsciente (la mujer) debe 
ser el puente entre los planos físico y espiritual. Esta simbología 
también muestra el verdadero poder del amor, pues a través del 
amor podemos mirar al Cielo.

69
Los Arcanos Mayores
Cuando en una lectura aparece la carta de los Amantes se 
suele referir a una relación y, cuando esto sucede, dicha relación 
será la expresión perfecta del amor entre dos personas. Será casi 
siempre una relación sexual, aunque puede no serlo. No obs-
tante, tenga siempre en mente la posibilidad de un conflicto, a 
pesar del feliz inicio. El amor es una llama que no debe dejarse 
desatendida; debe alimentarse y permitírsele arder todo el tiem-
po y con la brillantez que sea posible. Si no se trata de la unión 
física de un hombre y una mujer, los Amantes también pueden 
mostrar la integración de dos partes de usted mismo que están 
en conflicto, la masculina y la femenina. La combinación de 
ambas nos revelará una gran sabiduría.
Por último, esta carta implica la idea de elección, por lo 
general en el plano moral o ético. El ejemplo más común de esta 
elección es, tristemente, la elección entre su cónyuge y alguien 
más de quien usted se ha enamorado, aunque puede ser tam-
bién entre dos posibles compañeros, a los que ama, pero sólo 
uno de ellos puede ser el mejor para usted. Mire hacia dentro, y 
diríjase a su inconsciente en busca de inspiración. A través de él 
puede tener acceso a la sabiduría que necesita para que su elec-
ción sea la correcta, por el bien de todos los implicados. Confíe 
en el consejo de su Voz Interior y, una vez que haya tomado la 
decisión, no la cambie, cualquiera que sea la oposición a la que 
deba enfrentarse.
Significado:  Elección, tentación, atracción. La lucha entre el 
amor sagrado y el amor profano. Armonía de 
los aspectos interior y exterior de la vida. 
También amor puro en su expresión más eleva-
da. Altruismo.
Invertida:  El amor puede volvernos ciegos. Infidelidad, 
peleas. Intromisión de los padres. Posibilidad de 
realizar una mala elección. Puede también indi-
car la necesidad de estabilizar las emociones.

Los Arcano s May ores LA CARRO ZA La Carro za: El exit o, el tri un fo En ciert omo does un mister io el por que la Carro za, que es clara-  men te una carta de fue rza y control, has ido siempre asociada con el element oA gua. Peros u at rib uci on a Cancer es en real i dad vali-  dap or que esta carta tr at ademan era muy in tens a con las emo-  ci ones. La Carro za es una carta de control emo c ional: el p oder de lament e para adapt arlo s des eos del co razo ny di rigid or los haci a una expr es ion sign if i cat iv a. Noes el control emo c ional del Em per ad or, que el imina por comp leto to das sus emo ci ones en favor dela logic a yl a razon. El hombre que conduce la Carro za sabe ques use moci ones no de ben barrer sen i second ers ba jo la alf om bra, sino entre nar sey us arse paras u mayor bien estar.  71

El Tarot Universal de Waite
72
Con frecuencia, el triunfo sobre las emociones, tanto posi-
tivas como negativas, se muestra con dos esfinges, una blanca y 
la otra negra, que tiran de la Carroza. Si estuvieran sueltas 
correrían hacia cualquier dirección que ellas eligieran, pero aquí 
se mueven sólo hacia delante. Todavía tienen algo de poder, 
pero éste ahora lo dirige y lo enfoca el hombre que sostiene las 
riendas. La Carroza no puede moverse sin caballos o, en este 
caso, sin las esfinges que tiran de ella, así como nosotros no 
podemos movernos sin las emociones que nos motiven. Pero 
sin el control superior los caballos correrían libres, al igual que 
nuestras emociones cuando no se controlan. El equilibrio es 
necesario.
La Carroza personifica el tipo de disciplina necesaria para 
ganar control sobre las emociones, y por eso se eligió un símbo-
lo militar para esta carta. El propósito de las circunstancias seve-
ras que se dan en la milicia es desarrollar la voluntad y la habi-
lidad necesaria para controlar las emociones y usarlas de mane-
ra productiva en el campo de batalla. Sólo a través del dominio 
de sí mismo puede el hombre tener dominio sobre otros y sobre 
su entorno. La sabiduría y la gloria que se logran al conquistar a 
nuestros enemigos no es nada si la comparamos con el incre-
mento en la autoestima que experimentaremos al vencer nues-
tros miedos. Siempre es más difícil vencer a nuestros enemigos 
internos que a los externos, y sobre todo nos enseña mucho más.
Aplicando debidamente la fuerza de las emociones apren-
deremos a lograr nuestras metas con mayor rapidez. Alguien 
como el conductor de la Carroza, que tiene un control total sobre 
su voluntad y sus emociones, puede lograr casi cualquier cosa.
Con frecuencia la aparición de la Carroza muestra la nece-
sidad de tomar el control de nuestras emociones y, en lugar de 
gastar la energía en lamentaciones y quejas, usarla para llevar a 
cabo acciones y para realizar cambios en el mundo. El miedo lo 
debilitará, a menos que usted lo admita y lo enfrente. Entonces 
podrá usar su miedo de forma constructiva, para sus propias

Los Arcanos Mayores 
intenciones. A través del control de las emociones, nos dice la 
Carroza, aprendemos a controlarnos a nosotros mismos. 
Cuando haya alcanzado esa etapa, itodo es posible! Una 
vez que haya trascendido sus miedos empezará a trascender sus 
restricciones, hasta que nada lo pueda detener en su camino 
hacia el éxito que se merece. Con frecuencia, la aparición la 
Carroza es portavoz de la victoria. A través de la disciplina y la 
confianza, predice un momento en el que toda oposición será 
vencida. Si usted domina sus pasiones y cree en el poder de su 
voluntad, vendrán grandes éxitos y grandes logros. No permita 
que nada lo distraiga ni lo desvíe de sus objetivos, y proceda 
como el recto vuelo de una flecha. Nada está más allá de sus 
capacidades, si usted cree en su propio poder. 
Significado: 
Triunfo, éxito, victoria. Control sobre las fuerzas 
de la naturaleza. Recuperación de la salud, vic-
toria sobre las penurias económicas o sobre los 
enemigos de cualquier tipo. Es la carta de quie-
nes logran algo grande. Puede también signifi-
car viajes agradables y cómodos. 
Invertida: 
Victoria poco ética. Ambición excesiva y dema-
siado centrada en lo material. Derrota, desas-
tre, mala salud. Pobreza, necesidades. Frustra-
ción en una relación sexual. 
73

Los Arcanos May ores LA FUERZA LaFuerza: El dominio del esp i rita El t it u lode esta carta es enga no so, pu es la mayor i adel as per-  son as tien dena pens aren la fue rza como una prop i eda del cue rpo fi sico. Pero esta noes una carta de fue rza bruta, por que ninguno delos Arcano s May ores sea plica de man era direct a al cue rpo fi sico. Estas son cart as de ideas, sent i mien to sy cree n-  cias; tratar de h acer que una rcano Mayor represent ea al gui en con un cue rpo fuerte seria un s in sent ido. Pero la fue rza no si em-  pre se mi de en term in os de cu an to peso puede us ted lev an taro lo rapid o que pu eda corre r. LaVer dade ra Fortaleza es firm eza de car act er yl ahab ili dad no solo de control ar la semo ci ones,  75

76
El Tarot Universal de Waite
sino de mostrarse superior a ellas y triunfar sobre nuestros 
impulsos y deseos más bajos.
Esta carta continúa la lección de la Carroza, muestra que 
una vez que hemos aprendido a controlar las emociones, debe-
mos mostrarnos superiores a ellas. Muchas personas le atribuyen 
a esta carta la noción del perdón, de la compasión y de crianza, 
pero no es esto lo que se muestra con la Fortaleza. Es una carta 
de Fuego y, por lo tanto, perjudicial para todas las emociones. 
Las únicas cualidades que abundan en la Fortaleza son el valor 
y la paciencia. Ninguna de éstas es en realidad una emoción, 
sino que son maneras de actuar y de hacer, que no están miti-
gadas por los sentimientos. El valor es la antítesis del miedo; la 
paciencia, el control de los deseos mundanos. Aquí no existen 
emociones, sólo determinación y acción.
La simbología del león es común y muy apropiada para la 
Fortaleza. El león es la «bestia interior», el deseo violento que 
hay dentro de cada uno de nosotros y que debe ser controlado 
o de lo contrario se liberará para manifestarse al mundo. La ima-
gen de la mujer abriendo las fauces del león muestra tanto valor 
como paciencia; no debe temer al león y debe esperar a que se 
canse antes de poder ejercer su voluntad sobre él. Vemos plas-
mada en ella la pureza de la doncella y el poder de la bestia 
interior a la que ella trata de controlar.
Necesita paciencia para vencer al león, porque su poder no 
es la fuerza física bruta. Tiene muy poca fuerza, sin embargo 
puede aplicar una presión suave pero constante, y lo hará has-
ta que el león se someta a su voluntad superior. Muestra cierta 
determinación, y la convicción de que aun los resultados 
pequeños tendrán efectos si se mantienen lo suficiente, igual que 
un goteo constante agujerea una piedra. La Fortaleza no es una 
carta de compasión y amor, sino una carta de poder, calmado 
pero imparable. Ese poder irradia del alma, y para un estado 
consciente de este poder no puede haber resistencia ni derrota.

Los Arcanos Mayores 
Las cualidades de la Fuerza ya están en usted, esperan 
aparecer una vez que haya dominado todas sus emociones 
equivocadas y cuando esté listo para seguir hacia las tareas espi-
rituales que se encuentran más adelante. Su lección principal es 
que, si desea tomar consciencia de la sabiduría espiritual y de la 
intuición, las emociones deben ser trascendidas. Los murmullos de 
la intuición suelen ser ahogados por el rugido de la emoción, por 
la preocupación y el miedo. Sólo cuando éstos hayan sido elimi-
nados o silenciados podrá crearse el necesario silencio. Conquiste 
sus miedos, controle sus impulsos y nunca pierda la paciencia con 
usted mismo ni con lo que hace. Un día verá la sabiduría. 
La fuerza nos muestra a la mente dominando sobre la 
materia, a la voluntad superior sobre los deseos inferiores. No 
importa lo fuerte que parezca la bestia que hay en su interior, 
usted tiene el poder de controlarla y someterla a su voluntad. 
Esto no se puede hacer con fuerza física o con excesiva prisa; es 
un proceso lento y difícil. Sin embargo, cuando aparezca esta 
carta, puede estar seguro de que tendrá la resistencia suficiente 
para ver el final de esta tarea. Si está presionando con demasia-
da insistencia, la Fuerza nos muestra la necesidad de un retiro 
momentáneo y de ser paciente. El esclarecimiento vendrá sólo 
cuando sea el momento oportuno; no se puede apresurar. 
Significado: 
Fuerza de carácter, el poder espiritual venciendo 
al poder material. El amor triunfando sobre el 
odio. La naturaleza superior, sobre los deseos 
mundanos y carnales. 
Invertida: 
Dominio de lo material. Olvido de lo espiritual. 
Discordias. Carencia de fuerza moral. Abuso de 
poder. Temor a lo desconocido existente en uno 
mismo. 
77

Los Arcano s May ores EL ERM IT A NO ElE rmit a no: El guia et ero Cuando a nuestra men te veng an pre gun t as sobre la naturaleza dela exist en cia yelp r op osi to dela vida, las resp u estas no las en contra remo sen el mundo f is ico. So lo puede nen contra r seen nuestro interior. Siu st edse hae lev a do pore nci made sus des eos y de sus emo ci ones es por que es to syano le ser anu tiles ensu via je. Ahora es como el Erm it a no, que bus ca solo las resp u estas.  Des de a hora al Erm it a no solamente log uia ran los murmu l los de su V oz Interior yl alu z de su lamp ara. Enal gun moment o, tam bien abandon a rala lamp ara, por que es artificial y por lot an to temporal. Su prop i alu z interior de be a pre nder a brill ar, en a use nci adela luz deo tros.  79

El Tarot Universal de Waite 
Para que emerja la verdadera sabiduría, no puede haber 
distracciones. Cualquier preocupación mundana, sin importar 
lo pequeña o intrascendente que pueda parecer, se oirá como 
gritos que ahogan a la silenciosa luz interior. Pero también 
debemos librarnos de la confusión interior, no sólo de la exter­
na. El aislamiento y la separación del mundo son de gran ayuda. 
Éste es el sendero del Ermitano, que se introduce en la oscuridad 
para que la luz le sea revelada cuando esté preparado. Como el 
Loco, él está otra vez solo, separado de todos los demás. Pero 
esta vez no sólo es por elección, sino por necesidad. 
Usualmente, una vez que ha aprendido las lecciones y ha 
visto su verdadera sabiduría, el ermitano recoge su lámpara y 
vuelve al mundo real para ayudar a otros a que también sean 
concientes de su propio potencial. Pero el Ermitano no es un 
maestro, no instruirá a sus alumnos ni les hablará sobre sus 
experiencias de soledad y aislamiento. Deben experimentarlo 
por ellos mismos, ya que la sabiduría aprendida sólo escuchan­
do a otra persona no es sabiduría. La verdadera sabiduría y la 
verdadera iluminación siempre vienen del interior. Un maestro 
puede decirle a su alumno cómo encontró la sabiduría, pero el 
alumno deberá ir y encontrarla por sí mismo. La sabiduría no se 
regala. Se conquista con el sacrificio cotidiano y viviendo las 
experiencias que nos trae la vida. 
Pero las lecciones de la vida no pueden apresurarse, no 
pueden forzarse ni hacer que pasen antes de que sea su momen­
to. El conocimiento se convierte en sabiduría a través del sacri­
ficio. Todo lo que deje aquí, si decide seguir la llamada del 
Ermitano, permanecerá aquí a su regreso. Usted es el único que 
habrá cambiado. 
La aparición del Ermitano es una llamada a aprender más 
acerca de usted mismo y de la naturaleza de su existencia, y 
todas las personas reciben esta llamada en algún punto de sus 
vidas. Tómelo como una señal de que sus problemas y sus asuntos 
mundanos pueden esperar; hay un trabajo mayor, en su interior, 
80
   
"""

    # Inicializar LLMAgent
    # model = "gpt-3.5-turbo-0125"
    # model = "llama-3.3-70b-versatile"
    model = "gemma2-9b-it"
    # model = "mixtral-8x7b-32768" # No responde bien... 
    # model = "llama-3.1-8b-instant"
    # model = "llama3-8b-8192"
    llm_agent = LLMAgent(messages=[], llm_model=model)  # Cambia el modelo según tu preferencia

    # Inicializar DocumentProcessor
    processor = DocumentProcessor(llm_agent=llm_agent, max_tokens=2000)

    # Procesar el documento
    result = processor.process_document(raw_document)

    # Mostrar el resultado
    print(result)
