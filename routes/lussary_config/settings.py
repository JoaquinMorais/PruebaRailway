from flask import Blueprint,render_template,redirect,url_for,jsonify
from utils.db import db

from models.models import *
Home = Blueprint("Home",__name__)
def Insert(obj):
    db.session.add(obj)
    db.session.commit()

@Home.route("/")
def getHomePrincipalPageLussary():
    print(url_for('static',filename='css/clientes/Fermag/Proyectos/Señales_Debiles.webp'))
    return render_template("lussary_config/settings.html")

@Home.route("/home")
def getHome():
    return redirect(url_for('Home.getHomePrincipalPageLussary'))




@Home.route("/api")
def getExample():
    return jsonify({'message':'hello'})

@Home.route("/db/añadir")
def añadir():
    Insert(Persona('Alejo Luis', 'Diaz Broilo', ''))#1
    Insert(Persona('Agustín Jose', 'Salonia', ''))#2
    Insert(Persona('Marco', 'Fini Minué', ''))#3
    Insert(Persona('Máximo Tomas', 'Blazquez', ''))#4
    Insert(Persona('Joaquin', 'Morais', ''))#5
    Insert(Persona('Fernando Gabriel', 'Salonia', 'Ciente y principal comunicador de FERMAG'))#6
    
    Insert(Medio('Instagram',          'https://www.instagram.com/',    '/', 'instagram.svg'))#1
    Insert(Medio('GitHub',             'https://github.com/',           '',  'github.svg'))#2
    Insert(Medio('LinkedIn',           'https://ar.linkedin.com/in/',   '',  'linkedin.svg'))#3
    Insert(Medio('Correo Electronico', '',                              '',  'gmail.svg'))#4
    Insert(Medio('CHESS.COM',          'https://www.chess.com/member/', '',  'chess.svg'))#5
    
    Insert(Contacto(1, 1, 'alejo.diazbroilo'))#IG
    Insert(Contacto(2, 1, 'AlejoLuisDiazBroiloLussary'))#GIT
    Insert(Contacto(1, 2, 'agus04_Salonia'))#IG
    Insert(Contacto(2, 2, 'Salonia04'))#GIT
    Insert(Contacto(4, 2, 'agus'))
    Insert(Contacto(1, 3, 'marco_fm1'))#IG
    Insert(Contacto(2, 3, 'MarcoFm1'))#GIT
    Insert(Contacto(3, 3, 'marco-fini-minu%C3%A9-b35289275'))
    Insert(Contacto(1, 4, 'maximoblazquez'))#IG
    Insert(Contacto(1, 5, 'joa_mora05'))#IG
    Insert(Contacto(2, 5, 'JoaquinMorais'))#GIT
    Insert(Contacto(5, 5, 'joamora'))#CHESS
    
    Insert(Colaborador(1, '2004-07-18'))#1
    Insert(Colaborador(2, '2004-08-04'))#2
    Insert(Colaborador(3, '2005-03-22'))#3
    Insert(Colaborador(4, '2005-04-02'))#4
    Insert(Colaborador(5, '2005-03-27'))#5

    Insert(Actividad('backend', ''))#1
    Insert(Actividad('frontend', ''))#2
    Insert(Actividad('scram facilitator', ''))#3
    Insert(Actividad('economy', ''))#4
    Insert(Actividad('marketing', ''))#5
    Insert(Actividad('social media', ''))#6
    Insert(Actividad('diseño', ''))#7
    Insert(Actividad('database designer', ''))#8
    Insert(Actividad('testing', ''))#9
    Insert(Actividad('project manager', ''))#10

    Insert(Rol(1, 1))#Alejo
    Insert(Rol(1, 8))

    Insert(Rol(2, 2))#Salonia
    Insert(Rol(2, 6))
    Insert(Rol(2, 7))
    
    Insert(Rol(3, 2))#Fini
    Insert(Rol(3, 7))
    Insert(Rol(3, 5))
    Insert(Rol(3, 3))
    
    Insert(Rol(4, 9))#Facha
    Insert(Rol(4, 2))

    Insert(Rol(5, 1))#Mora
    Insert(Rol(5, 10))
    Insert(Rol(5, 4))

    Insert(DescripcionColaborador(1, 'Lugar de Nacimiento', 'BS. AS. Argentina'))#Alejo
    Insert(DescripcionColaborador(1, 'Telefono', '2915343727'))
    Insert(DescripcionColaborador(1, 'Discord', 'maruuu#2459'))
    Insert(DescripcionColaborador(1, 'Mail', 'diazbroiloalejol@gmail.com'))

    Insert(DescripcionColaborador(2, 'Telefono', '3513 99-2521'))
    Insert(DescripcionColaborador(2, 'Mail', 'agusalonia04@gmail.com'))

    Insert(DescripcionColaborador(3, 'Mail', 'marcofiniminuebusiness@gmail.com'))
    Insert(DescripcionColaborador(3, 'Telefono', '3518147051'))
    Insert(DescripcionColaborador(3, 'Discord', 'Marco_Fm1#1501'))

    Insert(DescripcionColaborador(4, 'Mail', 'maxi05blazquez@gmail.com'))
    Insert(DescripcionColaborador(4, 'Nick Riot', 'Facher05MB'))

    Insert(DescripcionColaborador(5, 'Lugar de Nacimiento', 'BS. AS. Argentina'))
    Insert(DescripcionColaborador(5, 'Mail', 'joaquinmorais2005@gmail.com'))
    


    Insert(Proyecto('Fermag', 'Lorem ut tortor vestibulum, eget suscipit leo consectetur.'))
    Insert(Proyecto('VEME', 'Lorem i ut tortor vestibulum, eget suscipit leo consectetur.'))
    Insert(SubProyecto(1, 'Domotica', 'servicio'))#1
    Insert(SubProyecto(1, 'BMS', 'servicio'))#2
    Insert(SubProyecto(1, 'Energias Renovables', 'servicio'))#3
    Insert(SubProyecto(1, 'Instalaciones Electricas', 'servicio'))#4
    Insert(SubProyecto(1, 'Señales Debiles', 'servicio'))#5
    Insert(SubProyecto(1, 'Todos', 'servicio'))#6
 
    Insert(Categoria('descripcion', 'varchar'))#1
    Insert(Categoria('INT', 'int'))#2
    Insert(Categoria('link', 'links'))#3
    Insert(Categoria('descripcion proyecto', 'descripciones uwu'))#4
    Insert(Categoria('ubicacion', 'link o coordenadas de ub'))#5
    Insert(Categoria('idframe ubicacion', 'link o coordenadas de ub'))#6
    Insert(Categoria('file', 'src'))#7
    Insert(Categoria('padre', 'este atributo tiene atributos relacionados'))#8

    #Servicios
    #Domotica
    Insert(AtributoGenerico('fondo_link', url_for('static',filename='src/clientes/Fermag/Proyectos/Domotica.webp'), 1, 7))#1
    #BMS
    Insert(AtributoGenerico('fondo_link', url_for('static',filename='src/clientes/Fermag/Proyectos/BMS.webp'), 2, 7))#2
    #Energias_Renovables
    Insert(AtributoGenerico('fondo_link', url_for('static',filename='src/clientes/Fermag/Proyectos/Energias_Renovables.webp'), 3, 7))#3
    #Instalaciones_Electricas
    Insert(AtributoGenerico('fondo_link', url_for('static',filename='src/clientes/Fermag/Proyectos/Instalaciones_Electricas.webp'), 4, 7))#4
    #Seniales_Debiles
    Insert(AtributoGenerico('fondo_link', url_for('static',filename='src/clientes/Fermag/Proyectos/Seniales_Debiles.webp'), 5, 7))#5
    #Todos
    Insert(AtributoGenerico('fondo_link', url_for('static',filename='src/clientes/Fermag/Proyectos/Todos.webp'), 6, 7))#6
    
    Insert(SubProyecto(1, 'CENTRO CULTURAL LOLA MORA', 'trabajo'))#7
    Insert(AtributoGenerico('descripcion', 'Ejecucion de Proyecto, provision e instalación de los siguientes sistemas:', 7, 8))#7
    
    Insert(AtributoDependiente('li', 'Generación Fotovoltaica', 7))
    Insert(AtributoDependiente('li', 'Generación Eólica', 7))
    Insert(AtributoDependiente('li', 'Sistema de control BMS (Building Management System)', 7))
    Insert(AtributoDependiente('li', 'Sistema de control de Accesos', 7))
    Insert(AtributoDependiente('li', 'Sistema de Vigilancia por Circuito Cerrado de TV (CCTV)', 7))
    Insert(AtributoDependiente('li', 'Sistema de Voz y Datos por IP', 7))
    Insert(AtributoDependiente('li', 'Sistema de Detección temprana de Incendio', 7))
    
    Insert(AtributoGenerico('detalles', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto con en CLIENTE y el estudio de arquitectura.', 7, 8))#8

    Insert(AtributoDependiente('li', 'Comando de iluminación ON/OFF y DIMMERS de áreas comunes.', 8))
    Insert(AtributoDependiente('li', 'Control de sistema de bombas sanitarias y alarmas de equipamiento tecnológico.', 8))
    Insert(AtributoDependiente('li', 'Control de riego en techo verde.', 8))
    Insert(AtributoDependiente('li', 'Provision e instalación de sistema de videoportero e interacción entre departamentos y guardia.', 8))
    Insert(AtributoDependiente('li', 'Detección de Incendios conforme a la normas NFPA  (National Fire Protection Association) con integración al sistem de BMS. Monitoreo de perdida de gas en cochera subterranea.', 8))
    Insert(AtributoDependiente('li', 'Control de extractores en cochera conforme a la calidad del aire.', 8))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP.', 8))

    
    Insert(AtributoGenerico('ubicacion', 'Ciudad de San Salvador de Jujuy', 7, 5))#9

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2017.4550447341242!2d-64.19172716287889!3d-31.406224551559028!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9432996ae064a587%3A0x9c4376fa2da800b5!2sTorre%20FLUSS!5e1!3m2!1ses-419!2sar!4v1683477989733!5m2!1ses-419!2sar', 7, 6))#10

    Insert(AtributoGenerico('año', '2021', 7, 2))#11

    Insert(AtributoGenerico('comitente', 'Nos contrata el Fideicomiso a cargo de la construcción luego de una actividad de Marketing de la Empresa.', 7, 1))#12
    
    #1_fondo
    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/1_fondo.webp'), 7, 7))#13

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 7, 8))#14

    #1_1
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/1_1.webp'), 14))
    #1_2
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/1_2.webp'), 14))
    #1_3
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/1_3.webp'), 14))
    #1_4
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/1_4.webp'), 14))

    Insert(SubProyecto(1, 'PLANTA CLOACAL BAJO GRANDE - CORDOBA', 'trabajo'))#8

    Insert(AtributoGenerico('descripcion', 'Ejecucion de Proyecto, provision e instalación de los siguientes sistemas:', 8, 8))# 15

    Insert(AtributoDependiente('li', 'Sistema de Vigilancia por Circuito Cerrado de TV (CCTV).', 15))    
    Insert(AtributoDependiente('li', 'Sistema de Voz y Datos por IP', 15))    
    Insert(AtributoDependiente('li', 'Sistema de Detección temprana de Incendio', 15))

    Insert(AtributoGenerico('detalles', 'Detalles del trabajo:', 8, 8)) #16

    Insert(AtributoDependiente('li', 'La instalación se caracteríza por un predio de varias hectarias donde los distintos puntos de control y supervisión se encontraba dispersos, lo que obligo al uso de la tecnología de Fibra Óptica para su interconexión. Esto requiió de un cableado estructurado desde donde se centró la comunicación de la información en lo que respecta a voz, datos y sistema de CCTV, realizado con cámaras de 4 y 8 MP controladas por NVRs distribuidas estratégicamente. ', 16))
    Insert(AtributoDependiente('li', 'El sistema de detección de incendios está basado en una configuración anillo conforme a lo establecido en las normativas NFPA (National Fire Protection Association).', 16))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Córdoba', 8, 5)) #17

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3405.4208146985156!2d-64.103904!3d-31.40252999999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMzHCsDI0JzA5LjEiUyA2NMKwMDYnMTQuMSJX!5e0!3m2!1ses-419!2sar!4v1683484492395!5m2!1ses-419!2sar', 8, 6)) #18

    Insert(AtributoGenerico('año', '2022', 8, 2)) #19

    Insert(AtributoGenerico('comitente', 'Nos confía esta obra la Empresa Constructora SUPERCEMENTO de la CABA0', 8, 1))# 20
    
    #2_fondo
    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/2_fondo.webp'), 8, 7))# 21

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 8, 8)) #22

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/2_1.webp'), 22))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/2_2.webp'), 22))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/2_3.webp'), 22))

    Insert(SubProyecto(1, 'CASA KOLBET', 'trabajo'))#9

    Insert(AtributoGenerico('descripcion', 'Casa unifamiliar donde se ralizó lo siguiente:', 9, 8))#23

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 23))
    Insert(AtributoDependiente('li', 'Instalaciones eléctricas y de señales débiles', 23))
    Insert(AtributoDependiente('li', 'Provision de tableros eléctricos', 23))
    Insert(AtributoDependiente('li', 'Configuración de la domótica', 23))

    Insert(AtributoGenerico('detalles', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto com el dueño y el estudio de arquitectura.', 9, 8))#24
    
    Insert(AtributoDependiente('li', 'Comando de todas la iluminación sea ON/OFF como DIMMER tanto interior como exterior.', 24))
    Insert(AtributoDependiente('li', 'Control y supervisión de bombas de riego y poscina.', 24))
    Insert(AtributoDependiente('li', 'Control de piso radiante y caldera de calefacción.', 24))
    Insert(AtributoDependiente('li', 'Alarmas de incendio, y calidad del aire interior.', 24))
    Insert(AtributoDependiente('li', 'Control de intrusión telesupervisada con cámaras de CCTV.', 24))
    Insert(AtributoDependiente('li', 'Control de acceso biométrico y RFID con APP.', 24))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP.', 24))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Santa Rosa de Calamuchita', 9, 5))#25

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3380.5721206254357!2d-64.52459049473924!3d-32.08081977841186!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMzLCsDA0JzUwLjIiUyA2NMKwMzEnMjcuNSJX!5e0!3m2!1ses-419!2sar!4v1683487174212!5m2!1ses-419!2sar', 9, 6))#26
    
    Insert(AtributoGenerico('año', '2022', 9, 2))#27

    Insert(AtributoGenerico('comitente', 'Nos contrata el propietario a raíz de recomendaciones de terceros', 9, 1))#28

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/3_fondo.webp'), 9, 7))#29

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 9, 8))#30

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/3_1.webp'), 30))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/3_2.webp'), 30))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/3_3.webp'), 30))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/3_4.webp'), 30))

    Insert(SubProyecto(1, 'CASA DITELLA', 'trabajo')) #10

    Insert(AtributoGenerico('descripcion', 'Casa unifamiliar donde se ralizó lo siguiente:', 10, 8))#31

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 31))
    Insert(AtributoDependiente('li', 'Instalaciones eléctricas y de señales débiles', 31))
    Insert(AtributoDependiente('li', 'Provision de tableros eléctricos', 31))
    Insert(AtributoDependiente('li', 'Instalacion de Paneles Solares FV Hibridos', 31))
    Insert(AtributoDependiente('li', 'Configuración de la domótica', 31))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 10, 8))#32

    Insert(AtributoDependiente('li', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto com el dueño y el estudio de arquitectura.', 32))
    Insert(AtributoDependiente('li', 'Comando de todas la iluminación sea ON/OFF como DIMMER tanto interior como exterior.', 32))
    Insert(AtributoDependiente('li', 'Control y supervisión de bombas de JCUZZI', 32))
    Insert(AtributoDependiente('li', 'Control de piso radiante y caldera de calefacción', 32))
    Insert(AtributoDependiente('li', 'Control de Aires Acondicionados', 32))
    Insert(AtributoDependiente('li', 'Alarmas de incendio, y calidad del aire interior', 32))
    Insert(AtributoDependiente('li', 'Control de intrusión', 32))
    Insert(AtributoDependiente('li', 'Control de acceso biométrico y RFID con APP', 32))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP', 32))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Córdoba', 10, 5))#33

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d504.6680593212634!2d-64.3100955063013!3d-31.3495605119051!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94329dde8a2fbf0b%3A0xaf373267c87005df!2sLa%20Rufina%20Club!5e1!3m2!1ses-419!2sar!4v1683490457901!5m2!1ses-419!2sar ', 10, 6))#34

    Insert(AtributoGenerico('año', '2022', 10, 2))#35

    Insert(AtributoGenerico('comitente', 'Hemos sido contratados por el propietario debido a nuestra relación previa y a nuestra experiencia en el campo correspondiente.', 10, 1))#36

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/4_fondo.webp'), 10, 7)) #37

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 10, 8))#38

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/4_1.webp'), 38))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/4_2.webp'), 38))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/4_3.webp'), 38))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/4_4.webp'), 38))

    Insert(SubProyecto(1, 'CASA CASTELVETRI', 'trabajo'))#11

    Insert(AtributoGenerico('descripcion', 'Departamento unifamiliar donde se ralizó lo siguiente:', 11, 8))#39

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 39))
    Insert(AtributoDependiente('li', 'Instalaciones eléctricas y de señales débiles', 39))
    Insert(AtributoDependiente('li', 'Provision de tableros eléctricos', 39))
    Insert(AtributoDependiente('li', 'Configuración de la domótica', 39))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto:', 11, 8))#40

    Insert(AtributoDependiente('li', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto com el dueño y el estudio de arquitectura.', 40))
    Insert(AtributoDependiente('li', 'Comando de todas la iluminación sea ON/OFF como DIMMER tanto interior como exterior.', 40))
    Insert(AtributoDependiente('li', 'Control y supervisión de bombas de riego y poscina', 40))
    Insert(AtributoDependiente('li', 'Control de calenatmiento piscina con termotanque solar', 40))
    Insert(AtributoDependiente('li', 'Control de piso radiante y caldera de calefacción', 40))
    Insert(AtributoDependiente('li', 'Alarmas de incendio, y calidad del aire interior', 40))
    Insert(AtributoDependiente('li', 'Control de intrusión telesupervisada con cámaras de CCTV', 40))
    Insert(AtributoDependiente('li', 'Control de acceso biométrico y RFID con APP', 40))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP', 40))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Córdoba', 11, 5))#41

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d3407.081268438092!2d-64.2569759498376!3d-31.35673652890569!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMzHCsDIxJzI0LjQiUyA2NMKwMTUnMjUuMSJX!5e0!3m2!1ses-419!2sar!4v1683492872683!5m2!1ses-419!2sar', 11, 6))#42

    Insert(AtributoGenerico('año', '2022', 11, 2))#43

    Insert(AtributoGenerico('comitente', 'Hemos sido contratados por el propietario debido a nuestras referencias, así como por la publicidad que ha sido difundida sobre nuestros servicios.', 11, 1))#44

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/5_fondo.webp'), 11, 7))#45

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 11, 8))#46

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/5_1.webp'), 46)) 
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/5_2.webp'), 46)) 
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/5_3.webp'), 46)) 
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/5_4.webp'), 46)) 

    Insert(SubProyecto(1, 'CASALGRANDE LAPLACE', 'trabajo'))#12

    Insert(AtributoGenerico('descripcion', 'Complejo habitacional de departamentos:', 12, 8))#47

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 47))
    Insert(AtributoDependiente('li', 'Instalaciones de domótica y de señales débiles', 47))
    Insert(AtributoDependiente('li', 'Provision de tableros eléctricos-domótico', 47))
    Insert(AtributoDependiente('li', 'Configuración de la domótica', 47))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 12, 8 ))#48

    Insert(AtributoDependiente('li', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto con CONECTAR y la Empresa Constructora DYCSA.', 48))
    Insert(AtributoDependiente('li', 'Comando de todas la iluminación sea ON/OFF como DIMMER en cada departamento', 48))
    Insert(AtributoDependiente('li', 'Control de calefacción y caldera.', 48))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP', 48))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Córdoba', 12, 5))#49

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d1009.2255210579872!2d-64.24752469132892!3d-31.359864660022787!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94329eb57e48f1f9%3A0x33f164223e2fb6ce!2sCASAGRANDE%20LAPLACE!5e1!3m2!1ses-419!2sar!4v1683501136255!5m2!1ses-419!2sar ', 12, 6))#50

    Insert(AtributoGenerico('año', '2022', 12, 2))#51

    Insert(AtributoGenerico('comitente', 'Estamos brindando servicios de asesoramiento y acompañamiento a la empresa Conectar en su relación comercial con el cliente DYCSA.', 12, 1))#52

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/6_fondo.webp'), 12, 7))#53

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 12, 8))#54

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/6_1.webp'), 54))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/6_2.webp'), 54))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/6_3.webp'), 54))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/6_4.webp'), 54))

####################################################################
    Insert(SubProyecto(1, 'TORRE FLUSS', 'trabajo'))#13

    Insert(AtributoGenerico('descripcion', 'Complejo habitacional de departamentos:', 13, 8))#55

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 55))
    Insert(AtributoDependiente('li', 'Instalaciones de BMS y de señales débiles', 55))
    Insert(AtributoDependiente('li', 'Provision de tableros de comandos en areas comunes', 55))
    Insert(AtributoDependiente('li', 'Configuración de BMS', 55))
    Insert(AtributoDependiente('li', 'Provision de videoporteros y CCTV', 55))
    Insert(AtributoDependiente('li', 'Control de riego de techo verde', 55))
    Insert(AtributoDependiente('li', 'Detección de Incendio y perdida de gas', 55))
    Insert(AtributoDependiente('li', 'Comandos de extractores', 55))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 13, 8 ))#56

    Insert(AtributoDependiente('li', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto con en CLIENTE y el estudio de arquitectura.', 56))
    Insert(AtributoDependiente('li', 'Comando de iluminación ON/OFF y DIMMERS de áreas comunes.', 56))
    Insert(AtributoDependiente('li', 'Control de sistema de bombas sanitarias y alarmas de equipamiento tecnológico.', 56))
    Insert(AtributoDependiente('li', 'Control de riego en techo verde', 56))
    Insert(AtributoDependiente('li', 'Provision e instalación de sistema de videoportero e interacción entre departamentos y guardia', 56))
    Insert(AtributoDependiente('li', 'Detección de Incendios conforme a la normas NFPA  (National Fire Protection Association) con integración al sistem de BMS. Monitoreo de perdida de gas en cochera subterranea', 56))
    Insert(AtributoDependiente('li', 'Control de extractores en cochera conforme a la calidad del aire', 56))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP', 56))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Córdoba', 13, 5))#57

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d8069.811910820949!2d-64.1936664!3d-31.4063207!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9432996ae064a587%3A0x9c4376fa2da800b5!2sTorre%20FLUSS!5e1!3m2!1ses-419!2sar!4v1683506501714!5m2!1ses-419!2sar', 13, 6))#58

    Insert(AtributoGenerico('año', '2021', 13, 2))#59

    Insert(AtributoGenerico('comitente', 'Nos contrata el Fideicomiso a cargo de la construcción luego de una actividad de Marketing de la Empresa.', 13, 1))#60

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/7_fondo.webp'), 13, 7))#61

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 13, 8))#62

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/7_1.webp'), 62))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/7_2.webp'), 62))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/7_3.webp'), 62))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/7_4.webp'), 62))
####################################################################
    Insert(SubProyecto(1, 'CASA LUDUEÑA', 'trabajo'))#14

    Insert(AtributoGenerico('descripcion', 'Complejo habitacional de departamentos:', 14, 8))#63

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 63))
    Insert(AtributoDependiente('li', 'Instalaciones eléctricas y de señales débiles', 63))
    Insert(AtributoDependiente('li', 'Provision de tableros eléctricos', 63))
    Insert(AtributoDependiente('li', 'Control de calefaccion y Aires Acondicinados', 63))
    Insert(AtributoDependiente('li', 'Configuración de la domótica', 63))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 14, 8 ))#64

    Insert(AtributoDependiente('li', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto com el dueño y el estudio de arquitectura.', 64))
    Insert(AtributoDependiente('li', 'Comando de todas la iluminación sea ON/OFF como DIMMER tanto interior como exterior.', 64))   
    Insert(AtributoDependiente('li', 'Control y supervisión de bombas de riego y poscina', 64))
    Insert(AtributoDependiente('li', 'Control de piso radiante y caldera de calefacción y Aires Acondicionados', 64))
    Insert(AtributoDependiente('li', 'Alarmas de incendio, y calidad del aire interior', 64))
    Insert(AtributoDependiente('li', 'Control de intrusión telesupervisada con cámaras de CCTV', 64))
    Insert(AtributoDependiente('li', 'Control de acceso biométrico y RFID con APP', 64))
    Insert(AtributoDependiente('li', 'Videoportero IP con APP', 64))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP', 64))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Villa Nueva - Córdoba', 14, 5))#65

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3989.5486472724124!2d-63.2235871!3d-32.4458359!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95cc426a2eb7bcaf%3A0x5c5ca576a790917c!2sLos%20Algarrobos!5e1!3m2!1ses-419!2sar!4v1684199539781!5m2!1ses-419!2sar', 14, 6))#66

    Insert(AtributoGenerico('año', '2021', 14, 2))#67

    Insert(AtributoGenerico('comitente', 'Nos contrata el propietario a raíz de recomendaciones de terceros', 14, 1))#68

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/8_fondo.webp'), 14, 7))#69

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 14, 8))#70

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/8_1.webp'), 70))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/8_2.webp'), 70))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/8_3.webp'), 70))


####################################################################

    Insert(SubProyecto(1, 'CASA VALINOTTO', 'trabajo'))#15

    Insert(AtributoGenerico('descripcion', 'Casa unifamiliar donde se ralizó lo siguiente:', 15, 8))#71

    Insert(AtributoDependiente('li', 'Proyecto electrico-domótico', 71))
    Insert(AtributoDependiente('li', 'Instalaciones eléctricas y de señales débiles', 71))
    Insert(AtributoDependiente('li', 'Provision de tableros eléctricos', 71))
    Insert(AtributoDependiente('li', 'Control de calefaccion y Aires Acondicinados', 71))
    Insert(AtributoDependiente('li', 'Provision de paneles solares FV', 71))
    Insert(AtributoDependiente('li', 'Configuración de la domótica', 71))


    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 15, 8 ))#72

    Insert(AtributoDependiente('li', 'La instalación se llevó a cabo bajo la supervisión de pesonal de nuestra Empresa y tras el desarrollo de un proyecto ejecutivo en conjunto com el dueño y el estudio de arquitectura.', 72))
    Insert(AtributoDependiente('li', 'Comando de todas la iluminación sea ON/OFF como DIMMER tanto interior como exterior.', 72))
    Insert(AtributoDependiente('li', 'Control y supervisión de bombas de riego y poscina', 72))
    Insert(AtributoDependiente('li', 'Control de piso radiante y caldera de calefacción y Aires Acondicionados', 72))
    Insert(AtributoDependiente('li', 'Alarmas de incendio, y calidad del aire interior', 72))
    Insert(AtributoDependiente('li', 'Control de temperatura y humedad en cava vinos', 72))
    Insert(AtributoDependiente('li', 'Control de intrusión telesupervisada con cámaras de CCTV', 72))
    Insert(AtributoDependiente('li', 'Control de acceso biométrico y RFID con APP', 72))
    Insert(AtributoDependiente('li', 'Videoportero IP con APP', 72))
    Insert(AtributoDependiente('li', 'Control y monitporeo a local y a distancia mediante APP', 72))
    Insert(AtributoDependiente('li', 'Instalacion de sistema de generación fotovoltaica hibrida de 5KVA', 72))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Villa Nueva - Córdoba', 15, 5))#73

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3989.5486472724124!2d-63.2235871!3d-32.4458359!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95cc426a2eb7bcaf%3A0x5c5ca576a790917c!2sLos%20Algarrobos!5e1!3m2!1ses-419!2sar!4v1684200336843!5m2!1ses-419!2sar', 15, 6))#74

    Insert(AtributoGenerico('año', '2020', 15, 2))#75

    Insert(AtributoGenerico('comitente', 'Nos contrata el propietario a raíz de recomendaciones de terceros', 15, 1))#76

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/9_fondo.webp'), 15, 7))#77

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 15, 8))#78

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/9_1.webp'), 78))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/9_2.webp'), 78))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/9_3.webp'), 78))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/9_4.webp'), 78))

####################################################################

    Insert(SubProyecto(1, 'INMeT - INSTITUTO DE MEDICINA TROPICAL IGUAZÚ', 'trabajo'))#16

    Insert(AtributoGenerico('descripcion', 'Ejecucion de Proyecto, provision e instalación de los siguientes sistemas:', 16, 8))#79

    Insert(AtributoDependiente('li', 'Sistema de control de Accesos', 79))
    Insert(AtributoDependiente('li', 'Sistema de Vigilancia por Circuito Cerrado de TV (CCTV)', 79))
    Insert(AtributoDependiente('li', 'Sistema de Voz y Datos por IP', 79))
    Insert(AtributoDependiente('li', 'Sistema de Detección temprana de Incendio', 79))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 16, 8 ))#80

    Insert(AtributoDependiente('li', 'Bloqueo de puertas de acceso a vestuarios para desinfección.', 80))
    Insert(AtributoDependiente('li', 'Comando y supervisión de luces animales.', 80))
    Insert(AtributoDependiente('li', 'Comando luces pasillos (efectos) y circulación.', 80))
    Insert(AtributoDependiente('li', 'Control de variables eléctricas.', 80))
    Insert(AtributoDependiente('li', 'Supervisión del sistema de suministro de energía y transferencia.', 80))
    Insert(AtributoDependiente('li', 'Supervisión de sistema de Detección de Incendios.', 80))
    Insert(AtributoDependiente('li', 'Supervisión de sistema de extinción de incendios.', 80))
    Insert(AtributoDependiente('li', 'Supervisión de sistema de bombeo sanitario.', 80))
    Insert(AtributoDependiente('li', 'Telesupervisión y control.', 80))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Puerto Iguazú', 16, 5))#81

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2130.9687994727487!2d-54.5811886!3d-25.6418426!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94f6925c8cb87c69%3A0x77e6daf89e6e4c70!2sInstituto%20Nacional%20de%20Medicina%20Tropical!5e1!3m2!1ses-419!2sar!4v1684203649347!5m2!1ses-419!2sar', 15, 6))#82

    Insert(AtributoGenerico('año', '2020', 16, 2))#83

    Insert(AtributoGenerico('comitente', 'La Empresa Constructora SUPERCEMENTO nos confió el proyecto realizado en la rovincia de Misiones. La obra tuvo la particularidad de dos suspensiones y nuestra Empresa estuvo a la altura de acompañar a la Empresa Constructora en superar las dificultades, llevando a buen puerto la finalización de la obra', 16, 1))#84

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/10_fondo.webp'), 16, 7))#85

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 16, 8))#86

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/10_1.webp'), 86))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/10_2.webp'), 86))
####################################################################

    Insert(SubProyecto(1, 'UNIVERSIDAD CATOLICA DE CORDOBA', 'trabajo'))#17

    Insert(AtributoGenerico('descripcion', 'FERMAG fue contratado para varias obras en todas las instalaciones que posee la UCC como:', 17, 8))#87

    Insert(AtributoDependiente('li', 'Adaptación de instalaciones eléctricas conforme a las normativas vigentes.', 87))
    Insert(AtributoDependiente('li', 'Obras Nuevas eléctricas', 87))
    Insert(AtributoDependiente('li', 'Obras nuevas de iluminación ornamental', 87))
    Insert(AtributoDependiente('li', 'Iluminación y domótica en auditorio Ingeniería', 87))
    Insert(AtributoDependiente('li', 'Certificaciones de Aptos eléctricos', 87))

    Insert(AtributoGenerico('detalles', 'Detalles del Proyecto', 17, 8 ))#88

    Insert(AtributoDependiente('li', 'Todas las obras fueron realizadas pajo la supervision de nuestra Empresa en conjunto con los departamentos de ingeniería de la UCC conforme a los máximos estándares del buen arte y las normatiuvas AEA y vigentes.', 88))
    Insert(AtributoDependiente('li', 'Se realizaron Instalaciones electricas, de señales débiles, cableados estructurados y domótica en distintos lugares, como asi tambien instalaciones especiales de iluminacion y audio', 88))

    Insert(AtributoGenerico('ubicacion', 'Ciudad de Córdoba y alrededores', 17, 5))#89

    Insert(AtributoGenerico('ubicacion_iframe', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d129126.4749941505!2d-64.27678470159081!3d-31.3994267401371!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9432985f478f5b69%3A0xb0a24f9a5366b092!2zQ8OzcmRvYmE!5e1!3m2!1ses-419!2sar!4v1684202668102!5m2!1ses-419!2sar', 17, 6))#90

    Insert(AtributoGenerico('año', '2018', 17, 2))#91

    Insert(AtributoGenerico('comitente', 'El comitente es directamente la UCC ', 17, 1))#92

    Insert(AtributoGenerico('fondo', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/11_fondo.webp'), 17, 7))#93

    Insert(AtributoGenerico('galeria_fotos', 'solo padre', 17, 8))#94

    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/11_1.webp'), 94))
    Insert(AtributoDependiente('imagen_galeria', url_for('static',filename='src/clientes/Fermag/TrabajosFermag/11_2.webp'), 94))
####################################################################
    Insert(SubDependencia(2,7))
    Insert(SubDependencia(4,7))
    Insert(SubDependencia(5,7))
    Insert(SubDependencia(6,7))

    Insert(SubDependencia(4,8))
    Insert(SubDependencia(5,8))
    Insert(SubDependencia(6,8))

    Insert(SubDependencia(1,9))
    Insert(SubDependencia(4,9))
    Insert(SubDependencia(5,9))
    Insert(SubDependencia(6,9))

    Insert(SubDependencia(1 ,10))
    Insert(SubDependencia(3,10))
    Insert(SubDependencia(4,10))
    Insert(SubDependencia(5,10))
    Insert(SubDependencia(6,10))

    Insert(SubDependencia(1,11))
    Insert(SubDependencia(3,11))
    Insert(SubDependencia(4,11))
    Insert(SubDependencia(5,11))
    Insert(SubDependencia(6,11))

    Insert(SubDependencia(1,12))
    Insert(SubDependencia(6,12))

    Insert(SubDependencia(2,13))
    Insert(SubDependencia(4,13))
    Insert(SubDependencia(5,13))
    Insert(SubDependencia(6,13))

    Insert(SubDependencia(1,14))
    Insert(SubDependencia(4,14))
    Insert(SubDependencia(5,14))
    Insert(SubDependencia(6,14))

    Insert(SubDependencia(1,15))
    Insert(SubDependencia(3,15))
    Insert(SubDependencia(4,15))
    Insert(SubDependencia(5,15))
    Insert(SubDependencia(6,15))

    Insert(SubDependencia(2,16))
    Insert(SubDependencia(4,16))
    Insert(SubDependencia(5,16))
    Insert(SubDependencia(6,16))

    Insert(SubDependencia(1,17))
    Insert(SubDependencia(2,17))
    Insert(SubDependencia(4,17))
    Insert(SubDependencia(5,17))
    Insert(SubDependencia(6,17))

    Insert(Area('hacer el models', 'hacer el model siguiendo el uml', 5))

    Insert(Contribucion(1, 1, 1,  "alejo pudo hacer el models, pendiente revision"))

    return redirect(url_for('Home.traer'))
"""
    Insert(SubProyecto(1, 'Domotica', 'servicio'))#1
    Insert(SubProyecto(1, 'UPS', 'servicio'))#2
    Insert(SubProyecto(1, 'Energias Renovables', 'servicio'))#3
    Insert(SubProyecto(1, 'Instalaciones Electricas', 'servicio'))#4
    Insert(SubProyecto(1, 'Señales Debiles', 'servicio'))#5
    Insert(SubProyecto(1, 'Todos', 'servicio'))#6
"""
"""
http://drive.google.com/uc?export=view&id=

"""

@Home.route("/db/traer")
def traer():
    x = 7
    query = SubProyecto.query.filter(SubProyecto.id_subproyecto.in_(db.session.query(SubDependencia.id_subpadre).filter_by(id_subhijo = x).subquery()), SubProyecto.titulo != 'Todos')
    for i in query:
        print(i.titulo)
    print("###########################################")
    return redirect(url_for('Home.getHome'))
