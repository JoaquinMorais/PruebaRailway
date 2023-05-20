from flask import Blueprint,render_template,redirect,url_for
from utils.db import db

CDL_servicios = Blueprint("CDL_servicios",__name__)


servicios = {
    'art': {
        'bg': 'https://cdn.computerhoy.com/sites/navi.axelspringer.es/public/media/image/2021/07/conducir-2409011.jpg?tf=1200x',
        'nombre': 'Traslado de ART',
        'descripcion': 'Transporte de personas que sufrieron accidentes de trabajo que necesitan trasladarse por motivos médicos, ya sea para realizar consultas, tratamientos o cirugías.',
        'transporte' : 'Vehículos especialmente acondicionados para el traslado de pacientes, con equipamiento médico de emergencia y personal capacitado para brindar atención sanitaria durante el traslado.',
        'cuidados': 'Se cuenta con personal capacitado y equipado con herramientas médicas y de rescate en caso de emergencias.',
        'lugar': 'Hospital o Centro médico',
        'btn': 'https://wa.me/5493516186600?text=Buenos%20dias,%20me%20gustaría%20reservar%20turno%20para%20servicio%20de%20traslado%20de%20art'


    },
    'discapacidad': {
        'bg': 'https://arc-anglerfish-arc2-prod-infobae.s3.amazonaws.com/public/X7GBEM6QFRHVZFVSVMHCTJH2WQ.jpg',
        'nombre': 'Traslado por discapacidad',
        'descripcion': 'Este servicio está diseñado para atender a personas que tienen alguna discapacidad física o mental, pueden ser niños, adolescentes o personas adultas.'
        ,'transporte' : 'Vehículos adaptados para personas con discapacidad, que pueden incluir rampas de acceso, elevadores o plataformas especiales para sillas de ruedas.',
        'cuidados': 'Cuidados y Asistencia especializada para pacientes con discapacidades, ya sea físicas o mentales, que requieren de un traslado seguro y cómodo.',
        'lugar': 'Su hogar, hasta un centro de rehabilitación, una cita médica, o cualquier otro lugar que necesiten.',
        'btn': 'https://forms.gle/VLUpMXdVGzYybCb96'


    },
    'adl': {
        'bg': 'https://cdn.discordapp.com/attachments/709860868720033867/1106573804555210752/parteambulancia.jpg',
        'nombre': 'Traslados Programados en Ambulancias de Baja Complejidad',
        'descripcion': 'Este servicio está diseñado para personas que necesitan ayuda para realizar las Actividades de la Vida Diaria (ADL), como vestirse, bañarse, comer o tomar medicamentos.'
        ,'transporte' : 'Ambulancias de baja complejidad, que son vehículos especialmente equipados para el traslado de pacientes que no requieren atención médica de emergencia. ',
        'cuidados': 'Brindan cuidados básicos de enfermería durante el traslado, como la medición de signos vitales y la administración de medicamentos.',
        'lugar': 'Clinica, Domicilio',
        'btn': 'https://wa.me/5493516186600?text=Buenos%20dias,%20me%20gustaría%20reservar%20turno%20para%20servicio%20de%20traslado%20de%20ambulancia'


    }
}

@CDL_servicios.route('/CDL/<servicio_id>')
def getCDLServicio(servicio_id):
    servicio = servicios.get(servicio_id, {'nombre': 'Servicio no encontrado', 'descripcion': ''})
    if servicio_id != 'art' and servicio_id != 'discapacidad' and servicio_id != 'adl':
        return redirect(url_for('CDL_home.CDLHome'))

    return render_template('/clientes/CDL/servicios.html', servicio=servicio, navbar = False)
    
