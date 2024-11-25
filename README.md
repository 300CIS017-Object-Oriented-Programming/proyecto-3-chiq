[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9bKkctvo)
# snies_proyecto_3
Proyecto_3



```mermaid
classDiagram
direction BT

class ProgramaAcademico{
    def __init__(self, )
        consolidados : Dict[int, Consolidado()]
        codigoDeLaInstitucion (int)
        iesPadre (int)
        institucionDeEducacionSuperiorIes (str)
        principalOSeccional  (str)
        idSectorIes  (int)
        sectorIes  (str)
        idCaracter  (int)
        caracterIes  (str)
        codigoDelDepartamentoIes  (int)
        departamentoDeDomicilioDeLaIes  (str)
        codigoDelMunicipioIes  (int)
        municipioDeDomicilioDeLaIes  (str)
        codigoSniesDelPrograma (int)
        programaAcademico  (str)
        idNivelAcademico (int)
        nivelAcademico  (str)
        idNivelDeFormacion  (int)
        nivelDeFormacion  (str)
        idMetodologia  (int)
        metodologia (str)
        idArea  (int)
        areaDeConocimiento (str)
        idNucleo  (int)
        nucleoBasicoDelConocimientoNbc  (str)
        idCineCampoAmplio  (int)
        descCineCampoAmplio  (str)
        idCineCampoEspecifico  (int)
        descCineCampoEspecifico  (str)
        idCineCodigoDetallado  (int)
        descCineCodigoDetallado  (str)
        codigoDelDepartamentoPrograma  (int)
        departamentoDeOfertaDelPrograma (str)
        codigoDelMunicipioPrograma(int)
        municipioDeOfertaDelPrograma(str)
}


  class SNIESController{
    def __init__(self)
        gestor_csv = GestorCSV()
        gestor_xlsx = GestorXLSX()
        gestor_json = GestorJSON()
        self.gestores: list[Gestor] = [gestor_csv, gestor_xlsx, gestor_json]
        self.programas_academicos: dict[int, ProgramaAcademico()]
}

class Propietario{
  -bool recibirHuesped
}

class Hogar{
  -string direccion
  -int numeroCamasDisponibles
  -bool alojarBebes
  -string descripcionHogar
  
}

Propietario <|-- Hogar
Persona <|-- Huesped
Persona <|-- Propietario



```
