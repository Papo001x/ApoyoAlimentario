from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from io import open
from datetime import datetime

lista=[]
lista2=[]
m_estudiantes=[]
estcarr=[]



def obtener():
    if str(combofacu.get())=='Artes':
        lista=['Arte Danzario','Artes Escénicas','Artes Musicales','Artes Plásticas y Visuales']
        combocarr['values']=lista
    elif str(combofacu.get())=='Ciencias y Educación':
        lista=['Archivística y Gestión de la Información Digital','Comunicación Social y Periodismo','Licenciatura en Biología','Licenciatura en Ciencias Sociales','Licenciatura en Educación Artística','Licenciatura en Lenguas Extranjeras con Énfasis en Inglés','Licenciatura en Matemáticas','Licenciatura en Física','Licenciatura en Humanidades y Lengua Castellana','Licenciatura en Educación Infantil','Licenciatura en Química','Matemáticas']
        combocarr['values']=lista
    elif str(combofacu.get())=='Ingenieria':
        lista=['Ingenieria Catastral y Geodesia','Ingenieria de Sistemas','Ingenieria Electronica','Ingenieria Electrica','Ingenieria Industrial']
        combocarr['values']=lista
    elif str(combofacu.get())=='Medio Ambiente y Recursos Naturales':
        lista=['Tecnología en Gestión Ambiental y Servicios Públicos','Tecnología en Saneamiento Ambiental','Tecnología en Levantamientos Topográficos','Administración Ambiental','Administración Deportiva','Ingeniería Ambiental','Ingeniería Forestal','Ingeniería Sanitaria','Ingenieria Topografica']
        combocarr['values']=lista
    elif str(combofacu.get())=='Tecnologíca':
        lista=['Tecnología en Gestión de la Producción Industrial por Ciclos Propedéuticos','Tecnología Electrónica por Ciclos Propedéuticos','Tecnología en Construcciones Civiles por Ciclos Propedéuticos','Tecnología en Sistemas Eléctricos de Media y Baja Tensión por Ciclos Propedéuticos','Tecnología en Sistematización de Datos por Ciclos Propedéuticos','Tecnología Mecánica por Ciclos Propedéuticos','Ingeniería Eléctrica por Ciclos Propedéuticos','Ingeniería en Control por Ciclos Propedéuticos','Ingeniería en Telecomunicaciones por Ciclos Propedéuticos','Ingeniería Civil por Ciclos Propedéuticos','Ingeniería de Producción por Ciclos Propedéuticos','Ingeniería en Telemática por Ciclos Propedéuticos','Ingeniería Mecánica por Ciclos Propedéuticos']
        combocarr['values']=lista

def get_datos_registro():
    nombre=str(txt.get())
    codigo=int(txt2.get())
    facultad=str(combofacu.get())
    carrera=str(combocarr.get())
    semestre=int(combosemestre.get())
    
    datos=str(nombre+','+str(codigo)+','+facultad+','+carrera+','+str(semestre))
    archivo_texto=open("datos_estudiantes.txt","r",encoding="utf-8")
    verificacion=archivo_texto.read()
    if verificacion=='':
        archivo_texto.close()
        archivo_texto=open("datos_estudiantes.txt","a",encoding="utf-8")
        archivo_texto.write(datos)
        archivo_texto.close()
    else:
        archivo_texto.close()
        archivo_texto=open("datos_estudiantes.txt","a",encoding="utf-8")
        archivo_texto.write('\n'+datos)
        archivo_texto.close()

window = Tk()
window.title('PROGRAMA DE APOYO ALIMENTARIO')
#control de ventanas
control_ventanas = ttk.Notebook(window)
reg_estudiantes= ttk.Frame(control_ventanas)
control_ventanas.add(reg_estudiantes, text='Registo estudiantes')
control_servicio=ttk.Frame(control_ventanas)
control_ventanas.add(control_servicio, text='Control uso del servicio')
consulta_registro=ttk.Frame(control_ventanas)
control_ventanas.add(consulta_registro, text='Consultar registro')
busqueda_estudiante=ttk.Frame(control_ventanas)
control_ventanas.add(busqueda_estudiante,text='Registro servicio')
#control de botones ventana registro estudiantes
lbl = Label(reg_estudiantes, text='Registro de estudiantes al apoyo alimentario', font=('Arial Bold', 25))
lbl2 = Label(reg_estudiantes, text='Nombre completo:', font=('Arial',10))
txt = Entry(reg_estudiantes,width=100) 
lbl3 = Label(reg_estudiantes, text='Codigo', font=('Arial',10))
txt2 = Entry(reg_estudiantes,width=11) 
lbl4 = Label(reg_estudiantes, text='Facultad',font=('Arial',10))
combofacu=Combobox(reg_estudiantes,state='readonly')
combofacu['values']=('Artes','Ciencias y Educación','Ingenieria','Medio Ambiente y Recursos Naturales','Tecnologíca')
lbl5 = Label(reg_estudiantes, text='Carrera',font=('Arial',10))
combocarr=Combobox(reg_estudiantes,state='readonly')
boton = Button(reg_estudiantes, text="seleccionar",command=obtener)
lbl6 = Label(reg_estudiantes,text='Semestre:',font=('Arial',10))
combosemestre=Combobox(reg_estudiantes,state='readonly')
combosemestre['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
botonreg = Button(reg_estudiantes,text='Registrar',command=get_datos_registro)


lbl.grid(column=0,row=0)
lbl2.grid(column=0,row=1)
txt.grid(column=1,row=1)
lbl3.grid(column=0,row=2)
txt2.grid(column=1,row=2)
lbl4.grid(column=0,row=3)
combofacu.grid(column=1,row=3)
lbl5.grid(column=0,row=4)
combocarr.grid(column=1,row=4)
boton.grid(column=2,row=3)
lbl6.grid(column=0,row=5)
combosemestre.grid(column=1,row=5)
botonreg.grid(column=1,row=6)

titulo=Label(busqueda_estudiante,text='Registro uso de servicio',font=('Arial Bold', 25))
titulo.grid(column=0,row=0)
lbel2=Label(busqueda_estudiante,text='Facultad',font=('Arial', 10))
lbel2.grid(column=0,row=1)
combo2facul=Combobox(busqueda_estudiante,state='readonly')
combo2facul['values']=('Artes','Ciencias y Educación','Ingenieria','Medio Ambiente y Recursos Naturales','Tecnologíca')
combo2facul.grid(column=1,row=1)
def obtener2():
    if str(combo2facul.get())=='Artes':
        lista2=['Arte Danzario','Artes Escénicas','Artes Musicales','Artes Plásticas y Visuales']
        combo2carr['values']=lista2
    elif str(combo2facul.get())=='Ciencias y Educación':
        lista2=['Archivística y Gestión de la Información Digital','Comunicación Social y Periodismo','Licenciatura en Biología','Licenciatura en Ciencias Sociales','Licenciatura en Educación Artística','Licenciatura en Lenguas Extranjeras con Énfasis en Inglés','Licenciatura en Matemáticas','Licenciatura en Física','Licenciatura en Humanidades y Lengua Castellana','Licenciatura en Educación Infantil','Licenciatura en Química','Matemáticas']
        combo2carr['values']=lista2
    elif str(combo2facul.get())=='Ingenieria':
        lista2=['Ingenieria Catastral y Geodesia','Ingenieria de Sistemas','Ingenieria Electronica','Ingenieria Electrica','Ingenieria Industrial']
        combo2carr['values']=lista2
    elif str(combo2facul.get())=='Medio Ambiente y Recursos Naturales':
        lista2=['Tecnología en Gestión Ambiental y Servicios Públicos','Tecnología en Saneamiento Ambiental','Tecnología en Levantamientos Topográficos','Administración Ambiental','Administración Deportiva','Ingeniería Ambiental','Ingeniería Forestal','Ingeniería Sanitaria','Ingenieria Topografica']
        combo2carr['values']=lista2
    elif str(combo2facul.get())=='Tecnologíca':
        lista2=['Tecnología en Gestión de la Producción Industrial por Ciclos Propedéuticos','Tecnología Electrónica por Ciclos Propedéuticos','Tecnología en Construcciones Civiles por Ciclos Propedéuticos','Tecnología en Sistemas Eléctricos de Media y Baja Tensión por Ciclos Propedéuticos','Tecnología en Sistematización de Datos por Ciclos Propedéuticos','Tecnología Mecánica por Ciclos Propedéuticos','Ingeniería Eléctrica por Ciclos Propedéuticos','Ingeniería en Control por Ciclos Propedéuticos','Ingeniería en Telecomunicaciones por Ciclos Propedéuticos','Ingeniería Civil por Ciclos Propedéuticos','Ingeniería de Producción por Ciclos Propedéuticos','Ingeniería en Telemática por Ciclos Propedéuticos','Ingeniería Mecánica por Ciclos Propedéuticos']
        combo2carr['values']=lista2
boton2=Button(busqueda_estudiante,text='Seleccionar',command=obtener2)
boton2.grid(column=1,row=2)
lbel3=Label(busqueda_estudiante,text='Carrera',font=('Arial', 10))
lbel3.grid(column=2,row=1)
combo2carr=Combobox(busqueda_estudiante,state='readonly')
combo2carr.grid(column=3,row=1)


def bus_es_carrera():
    m_estudiantes=[]
    estcarr=[]
    estudiantesls=open("datos_estudiantes.txt","r",encoding="utf-8")
    txts=estudiantesls.read()
    estudiantesls.close()
    ls=txts.split('\n')
    for val in ls:
        m_estudiantes.append(val.split(','))
    for est in m_estudiantes:
        if est[3]==combo2carr.get():
            estcarr.append(est[0])
    comboest['values']=estcarr     

def obtenerfecha():
    fecha=datetime.now()
    lbel6=Label(busqueda_estudiante,text='Registrado con la fecha:')
    lbel6.grid(column=0,row=4)
    lbel5=Label(busqueda_estudiante,text=str(fecha))
    lbel5.grid(column=1,row=4)
    facx=str(combo2facul.get())
    nombx=str(comboest.get())
    fecx=str(fecha)
    datsox=str(nombx+','+facx+','+fecx)
    usdiario=open('Uso_diario.txt','r',encoding='utf-8')
    basedia=usdiario.read()
    usdiario.close()
    usdiario=open('Uso_diario.txt','a',encoding='utf-8')
    if basedia=='':
        usdiario.write(datsox)
        usdiario.close()
    else:
        usdiario.write('\n'+datsox)
        usdiario.close()        

def get_consulta():
    label5.configure(text='')
    label6.configure(text='')
    label7.configure(text='')
    otralista=[]
    persona=[]
    lafecha=[]
    lafacultad=[]
    mesconsulta=str(c_mes.get())
    diaconsulta=str(c_dia.get())
    añoconsulta=str(txt2asd.get())
    fechaconsulta=str(añoconsulta+'-'+mesconsulta+'-'+diaconsulta)
    usodiario=open('Uso_diario.txt','r',encoding="utf-8")
    datax=usodiario.read()
    usodiario.close()
    lsdata=datax.split('\n')
    for datals in lsdata:
        otralista.append(datals.split(','))
    for reco in otralista:
        if fechaconsulta in reco[2]:
            persona.append(reco[0])
            lafacultad.append(reco[1])
            lafecha.append(reco[2])
                
    label5.configure(text='\n'.join(map(str,persona)))
    label6.configure(text='\n'.join(map(str,lafacultad)))
    label7.configure(text='\n'.join(map(str,lafecha)))

def boton1x():
    otralista=[]
    contador=0
    fechaconsulta=str(elaño.get()+'-'+comboelmes.get()+'-'+comboeldia.get())
    usodiario=open('Uso_diario.txt','r',encoding="utf-8")
    datax=usodiario.read()
    usodiario.close()
    lsdata=datax.split('\n')
    for datals in lsdata:
        otralista.append(datals.split(','))
    for reco in otralista:    
        if fechaconsulta in reco[2]:
            contador=contador+1
    cadena=str('El dia '+fechaconsulta+', '+str(contador)+' personas usaron el servicio')
    contadorxd=Label(control_servicio,text=cadena)
    contadorxd.grid(column=0,row=2)

def boton2x():
    otralista=[]
    contador=0
    fechaconsulta=str(elaño1.get()+'-'+comboelmes1.get())
    usodiario=open('Uso_diario.txt','r',encoding="utf-8")
    datax=usodiario.read()
    usodiario.close()
    lsdata=datax.split('\n')
    for datals in lsdata:
        otralista.append(datals.split(','))
    for reco in otralista:    
        if fechaconsulta in reco[2]:
            contador=contador+1
    cadena=str('Durante el mes usaron el servicio '+str(contador))
    contadorxd1=Label(control_servicio,text=cadena)
    contadorxd1.grid(column=0,row=3)

def boton3x(): 
    otralista=[]
    contador=0
    fechaconsulta=str(elaño1.get()+'-')
    usodiario=open('Uso_diario.txt','r',encoding="utf-8")
    datax=usodiario.read()
    usodiario.close()
    lsdata=datax.split('\n')
    for datals in lsdata:
        otralista.append(datals.split(','))
    for reco in otralista:    
        if fechaconsulta in reco[2]:
            contador=contador+1
    cadena=str('Durante el año usaron el servicio '+str(contador))
    contadorxd2=Label(control_servicio,text=cadena)
    contadorxd2.grid(column=0,row=4)

boton3=Button(busqueda_estudiante,text='Seleccionar',command=bus_es_carrera)
boton3.grid(column=3,row=2)
lbel4=Label(busqueda_estudiante,text='Estudiante',font=('Arial', 10))
lbel4.grid(column=4,row=1)
comboest=Combobox(busqueda_estudiante,state='readonly')
comboest.grid(column=5,row=1)
boton4=Button(busqueda_estudiante,text='Guardar',command=obtenerfecha)
boton4.grid(column=6,row=1)

label1=Label(consulta_registro,text='Consulta registro del apoyo alimentario', font=('Arial Bold', 25))
label1.grid(column=0,row=0)
label2=Label(consulta_registro,text='Mes')
label2.grid(column=0,row=1)
c_mes=Combobox(consulta_registro,state='readonly')
c_mes.grid(column=1,row=1)
c_mes['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
label3=Label(consulta_registro,text='Dia')
label3.grid(column=0,row=2)
c_dia=Combobox(consulta_registro,state='readonly')
c_dia.grid(column=1,row=2)
c_dia['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
label4=Label(consulta_registro,text='Año')
label4.grid(column=0,row=3)
txt2asd= Entry(consulta_registro,width=23)
txt2asd.grid(column=1,row=3) 
 
botonbus=Button(consulta_registro,text='Buscar',command=get_consulta)
botonbus.grid(column=2,row=2)  
nombrel=Label(consulta_registro,text='Nombre estudiante',font=('Arial Bold', 12))
facultal=Label(consulta_registro,text='Facultad',font=('Arial Bold', 12))
horal=Label(consulta_registro,text='Fecha y hora',font=('Arial Bold', 12))
nombrel.grid(column=0,row=5)
facultal.grid(column=1,row=5)
horal.grid(column=2,row=5)
label5=Label(consulta_registro,text='')
label5.grid(column=0,row=6)
label6=Label(consulta_registro,text='')
label6.grid(column=1,row=6)
label7=Label(consulta_registro,text='')
label7.grid(column=2,row=6)

#Estadisticas del sistema

labex1=Label(control_servicio,text='Estaditicas de uso de servicio', font=('Arial Bold', 25))
labex1.grid(column=0,row=0)
elmes=Label(control_servicio,text='Mes')
comboelmes=Combobox(control_servicio,state='readonly')
comboelmes['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
eldia=Label(control_servicio,text='Dia')
comboeldia=Combobox(control_servicio,state='readonly')
comboeldia['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
el_año=Label(control_servicio,text='Año')
elaño=Entry(control_servicio,width=23)
labelxd=Label(control_servicio,text='Uso de servicio por dia: ',font=('Arial Bold',10))
botonrad=Button(control_servicio,text='Seleccionar',command=boton1x)
botonrad.grid(column=8,row=2)
labelxd.grid(column=1,row=2)
elmes.grid(column=2,row=2)
comboelmes.grid(column=3,row=2)
eldia.grid(column=4,row=2)
comboeldia.grid(column=5,row=2)
el_año.grid(column=6,row=2)
elaño.grid(column=7,row=2)
labelxd1=Label(control_servicio,text='Uso de servicio por mes: ',font=('Arial Bold',10))
labelxd1.grid(column=1,row=3)
comboelmes1=Combobox(control_servicio,state='readonly')
comboelmes1['values']=('01','02','03','04','05','06','07','08','09','10','11','12')
comboelmes1.grid(column=3,row=3)
elmes1=Label(control_servicio,text='Mes')
elmes1.grid(column=2,row=3)
el_año1=Label(control_servicio,text='Año')
elaño1=Entry(control_servicio,width=23)
el_año1.grid(column=4,row=3)
elaño1.grid(column=5,row=3)
botonrad1=Button(control_servicio,text='Seleccionar',command=boton2x)
botonrad1.grid(column=8,row=3)
labelxd2=Label(control_servicio,text='Uso de servicio por año: ',font=('Arial Bold',10))
labelxd2.grid(column=1,row=4)
el_año2=Label(control_servicio,text='Año')
elaño2=Entry(control_servicio,width=23)
el_año2.grid(column=2,row=4)
elaño2.grid(column=3,row=4)
botonrad2=Button(control_servicio,text='Seleccionar',command=boton3x)
botonrad2.grid(column=8,row=4)

control_ventanas.pack(expand=1, fill='both')  
window.mainloop()
