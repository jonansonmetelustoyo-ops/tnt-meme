# recordar descargar flet 
#recuerda sacar este archivo al escritorio 


import flet as aplicacion 
import os 

 ############################################################################# variavles globales ###########################################################################
numero_de_meme = -1
numero_de_elemento = -1
rutas = []
 ##########################################################################################################################################################################################
 



 ################################################################## esto cuenta cuantos memes tienes guardados para comesar a ejecutar la app ###############################################################################
cuantos_memes_hay = []

for raiz, directorios, archivos in os.walk('C:\\Users\\djinventos\\Desktop\\tnt\\mis_memes'):#  C:\\Users\\DELL\\OneDrive\\Escritorio\\mis_memes\\
    for archivo in archivos:
       cuantos_memes_hay.append(os.path.join(raiz, archivo))


print(len(cuantos_memes_hay))
 ##########################################################################################################################################################################################



 ################################################################## MI_FUNCION_PRINCIPAL ##############################################################################
def MI_FUNCION_PRINCIPAL(hoja:aplicacion.Page):

    hoja.bgcolor = "black"
    hoja.title = "Tnt Memes - version 6.3.0"
    hoja.vertical_alignment = "center"
    hoja.horizontal_alignment = "center"
    escrol = aplicacion.ListView(expand = True ,spacing = 50,padding = 300)
    global rutas
    global cuantos_memes_hay

      #################################################################### esta funcion pone las ventanas y los memes ###############################################################################
    def ventanas_y_memes():
      ############################################################################# esto son variables globales ################################################################################
      global cuantos_memes_hay
      global numero_de_elemento
      numero_de_elemento += 1
      global rutas
      rutas
      global numero_de_meme
      numero_de_meme = numero_de_elemento
      ##########################################################################################################################################################################################
      
      
      
      ############################################################## esto guarda cada direccion de meme en una lista  #######################################################################################
      for raiz, directorios, archivos in os.walk('C:\\Users\\djinventos\\Desktop\\tnt\\mis_memes'):#  C:\\Users\\DELL\\OneDrive\\Escritorio\\mis_memes\\    
        for archivo in archivos:
          rutas.append(os.path.join(raiz , archivo))
     ##########################################################################################################################################################################################
     
      
        
      ################################################################# esto hace un iteracion en cada elemento #############################################################################
      rut = rutas[numero_de_elemento] 
      ##########################################################################################################################################################################################
      
      ################################################################### esto combierte la direccion en una imagen #################################################################################
      imagen = aplicacion.Image(src = rut ,width = 3000,height =490) 
      ##########################################################################################################################################################################################
      
      ################################################################### esto es el numero de meme ###########################################################################
      texto = aplicacion.Text(value = "meme numero  "+str(numero_de_meme),size = 20)
      ##########################################################################################################################################################################################
      
      ################################################################## esto es la ventana con el degradado y sus elementos ##########################################################################################
      ventana = aplicacion.Column([texto,imagen],alignment = aplicacion.MainAxisAlignment.CENTER) 
      fondo_con_borde = aplicacion.Container (content = ventana,border_radius = 20,  width = 3000, height = 599,gradient = aplicacion.LinearGradient([ aplicacion.Colors.RED,aplicacion.Colors.PINK,aplicacion.Colors.PURPLE]))
      columna_principal = aplicacion.Column([fondo_con_borde],alignment = aplicacion.CrossAxisAlignment.CENTER )
     ##########################################################################################################################################################################################
     
     ################################################################# esto agrega el fondo con borde y el meme con numero al escrol ##########################################################################
      aplicando_el_escrol_a = [columna_principal]   
      escrol.controls.extend(aplicando_el_escrol_a)
      ##########################################################################################################################################################################################

         
         
    
    
      hoja.update() 
      pass
   ##########################################################################################################################################################################################
    
   
    
   
    
   ################################################################################## esta funcion  borra memes #############################################################################
    def borar_memes(event):
        
        ##################################### esto contiene los datos de los dos botones : -> quitar_texto y BORRAR #############################################################################
        accion = event.control.data
        ##########################################################################################################################################################################################
        
        
        ######################################################## todo esto pasa si se pulsa borrar ##############################################################################################
        if accion == "DELETE":
          if barra_de_busqueda.value:
            barra_de_busqueda.value
            tengo_que_eliminar_el_meme_numero = rutas[int(barra_de_busqueda.value)]
            os.remove(str(tengo_que_eliminar_el_meme_numero))
            rutas.remove(tengo_que_eliminar_el_meme_numero)
            testo.value = "meme ELIMINADO con exito reiniciar la app para notar los cambios "
            print(tengo_que_eliminar_el_meme_numero)
        ##########################################################################################################################################################################################
            
        ############################################################## todo esto pasa si se pulsa quitar_texto ##################################################################################
        if accion == "QUITAR_TEXTO":
            testo.value = ""
       ##########################################################################################################################################################################################
        
        
        hoja.update()
                
         
        pass
    ##########################################################################################################################################################################################
    
    ################################### esto cuenta cuantos memes tienes y pone el texto de un color o otro dependiendo de cuantos tengas ####################################################
    def contador_de_memes():
      
       
        
       ############################################################# esto le pone una (s) a el texto  meme si no es uno ###########################################################################
        
        men = " meme"
        if len(cuantos_memes_hay) == 1:
            men = " meme"
        else:
            men = " memes"
        ##########################################################################################################################################################################################
         
        
        ##########################################################esto es el texto base ##########################################################################################################
        cuantos_memes_tengo = aplicacion.Text(value ="tengo " + str(len(cuantos_memes_hay)) + men ,size = 20)
        ##########################################################################################################################################################################################
         
        
        ######################### esto hace que dependiendo de cuantos memes tengas el texto se ponga de un amarillo o rojo como avertencia #######################################################
         
        if len(cuantos_memes_hay) >= 50:
            cuantos_memes_tengo = aplicacion.Text(value ="tengo " + str(len(cuantos_memes_hay)) + men ,size = 20,color = aplicacion.Colors.YELLOW)
        
        if len(cuantos_memes_hay) >= 90:
            cuantos_memes_tengo = aplicacion.Text(value ="tengo " + str(len(cuantos_memes_hay)) + men ,size = 20,color = aplicacion.Colors.RED)
       ##########################################################################################################################################################################################
     
    
        return cuantos_memes_tengo
    
        pass
        
        
        
    ##########################################################################################################################################################################################
        
       
    

    ################ ( esto ejecuta la app )dependiendo de si tienes memes esto mostrara esos memes  pero si no mostrara una notificacion de que notienes memes  #####################################################################################
    if len(cuantos_memes_hay) > 0 :
     for cargar_imagenes in range(len(cuantos_memes_hay)):
         ventanas_y_memes()
    
    elif len(cuantos_memes_hay) == 0 :
         ############################################################### direccion de le notificacion #############################################################################################
         imagen2 = aplicacion.Image(src = "C:\\Users\\djinventos\\Desktop\\tnt\\notificacion\\notificacion.png " ,width = 3000,height =490) #  C:\\Users\\DELL\\OneDrive\\Escritorio\\notificaciones_tnt\\Z_Tnt_Meme_tedice.png  
         ##########################################################################################################################################################################################
         
         ############################################################### esto es la ventana con degradado #########################################################################################
         ventana = aplicacion.Column([imagen2],alignment = aplicacion.MainAxisAlignment.CENTER) 
         fondo_co_borde = aplicacion.Container (content = ventana,border_radius = 20,  width = 3000, height = 599,gradient = aplicacion.LinearGradient([ aplicacion.Colors.RED,aplicacion.Colors.PINK,aplicacion.Colors.PURPLE]))
         columna = aplicacion.Column([fondo_co_borde],alignment = aplicacion.CrossAxisAlignment.CENTER )
         aplicando_escrol_a = [columna]
         escrol.controls.extend(aplicando_escrol_a)
         ##########################################################################################################################################################################################
     
    #####################################################################################################################################################################################################################
    
    
    
    
    
    
    
    ############################################################ esto es la sub notificacion que aparese al lado de la barra_de_busqueda  ##########################################################
    testo = aplicacion.Text(value = "")
    
    quitar_texto = aplicacion.IconButton(aplicacion.Icons.CANCEL,icon_color = aplicacion.Colors.RED,on_click = borar_memes,data = "QUITAR_TEXTO")# quitar texto 
    fila = aplicacion.Row([quitar_texto,testo,contador_de_memes()])
    ###############################################################################################################################################################################################
    
    
    ######################################   esto son los elementos para borrar un meme espesifico  ##############################################################################
    barra_de_busqueda = aplicacion.TextField(value="",hint_text = "escribe el numero del meme ", text_align=aplicacion.TextAlign.CENTER, width=300)#[input text]
    BORRAR = aplicacion.IconButton(aplicacion.Icons.DELETE,icon_color = aplicacion.Colors.RED,on_click = borar_memes,data = "DELETE") # BORRAR
    fila_consola = aplicacion.Row([barra_de_busqueda,BORRAR]) # fila 
    ################################################################################################################################################################################
   
    ################################################ esto esla barra y aplica sus elementos ########################################################################################
    fila_con_elementos = aplicacion.Row([fila_consola,fila],alignment = aplicacion.CrossAxisAlignment.CENTER)
    barra = aplicacion.Container ( fila_con_elementos ,width = 10000, height = 60,border_radius = 5,bgcolor = aplicacion.Colors.ON_ERROR,padding = 10)
    #################################################################################################################################################################################
      
      
   
  
    
    hoja.add(escrol,barra)
    # fin de la funcion principal 
    pass
########################################################################################################################################################################################## 


################################################################# esto ejecuta la funcion principal ############################################################################
aplicacion.run(MI_FUNCION_PRINCIPAL) # PC
#aplicacion.app(target = MI_FUNCION_PRINCIPAL, view=aplicacion.AppView.WEB_BROWSER, port = 100) # WEB
##########################################################################################################################################################################################








