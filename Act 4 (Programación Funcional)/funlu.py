#########################Función para cargar un archivo como un dataframe############
#1 CARGA DE ARCHIVO
def cargar_dataset(archivo):
    import pandas as pd
    import os

    #si se desea agregar un input se coloca:
    #Archivo = input("Favor ingresa el nombre del archiv")
    extension = os.path.splitext(archivo)[1].lower()   #Al archivo se le saca la extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return (df)
    elif extension == '.xlsx':
        df =pd.read_excel(archivo)
        return(df)
    elif extension == '.json':
        df = pd.read_json(archivo)
        return (df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return (df)
    else:
            raise ValueError(f"Formato de archivo no soportado: {extension}")
    

############################################################################################3

#2 SUSTITUIR POR FORWARD FILL para cualitativas 
def sustitución_ffill(df):
    import pandas as pd
    import os
    
    #Separo columnas cuantitativas del dataframe
    cuantitativas = df.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = df.select_dtypes(include=['object'])
    #Sustituir valores nulos con promedio o media
    cualitativas = cualitativas.fillna(method='ffill')

    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
    

##############################################################################################
#3 RELLENAR DATOS BACKWARD para cualitativas 
def sustitución_bfill(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cualitativas = cualitativas.fillna(method='bfill')


    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)


#####################################################
#4 STRING EN CONCRETO para cualitativas 
def sustitución_string(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])
    
    cualitativas = cualitativas.fillna("NO HAY DATOS")

    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

########################################################################33
#5 PROMEDIO MÉTODO para cuantitativas 
def sustitución_promedio(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(round(cuantitativas.mean(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

############################################################################
#6 MEDIANA MÉTODO para cuantitavivas 

def sustitución_mediana(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(round(cuantitativas.median(), 1))
    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)


###############################################
#7 MÉTODO CONSTANTE para cuantitativas 

def sustitución_int(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas_con_nulos = data.select_dtypes(include='int64')
    #Separo columnas cualitativas del dataframe
    
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas_con_nulos.fillna(0000)

    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas], axis=1)
    
    return(Datos_sin_nulos)

############################################
#8 IDENTIFICAR VALORES NULOS POR COLUMNA Y POR DATAFRAME

def cuenta_valores_nulos(dataframe):
    #Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    #Valores nulos por dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()
    
    return("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)


########################################################3
#MÁS ESPECÍFICAS 

##########################################################33
##Para columnas númericas  que quieran rellenarse con .mean 
def fill_numeric(data, col):
    #Rellena valores nulos en columnas numéricas con la media.
    data[col] = data[col].fillna(round(data[col].mean(), 1))
    return data

############################################333
##Rellena las columnas con ffill dpendiendo de cual columna quieras, no importa si es númerica o object

def fill_categorical(data, col):
    import pandas as pd
    data[col] = data[col].fillna(method="ffill")
    return data
###########################################################################33
##Rellena las columnas con ffill dpendiendo de cual columna quieras, no importa si es númerica o object

def fill_with_bfill(data, col):
    data[col] = data[col].fillna(method="bfill")
    return data

##################################################################3

#Rellenar con strings
#Value si queire que sea string debe ponerse entre comillas sino será una constante númerica
def fill_with_value(data, col, value):
    data[col] = data[col].fillna(value)
    return data


###############################################################
#Rellena .median 
def fill_with_median(data, col):
    data[col] = data[col].fillna(round(data[col].median(), 1))
    return data


################################################################3


######Sustituye todos los datos nulos con contantes y bfill

def sustitución_completa(data):
    import pandas as pd
    #Separo columnas cuantitativas del dataframe
    cuantitativas = data.select_dtypes(include=['float64', 'int64','float','int'])
    #Separo columnas cualitativas del dataframe
    cualitativas = data.select_dtypes(include=['object', 'datetime','category'])
    #Sustituir valores nulos con promedio o media
    cuantitativas = cuantitativas.fillna(0000)
    cualitativas = cualitativas.fillna('sin datos')

    # Unimos el dataframe cuantitativo limpio con el dataframe cualitativo
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)
