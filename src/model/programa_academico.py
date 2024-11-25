
from consolidado import Consolidado
from typing import Dict

class ProgramaAcademico:

    # Atributos

    consolidados: Dict[int, Consolidado] 
    codigoDeLaInstitucion: int
    iesPadre: int
    institucionDeEducacionSuperiorIes: str
    principalOSeccional: str
    idSectorIes: int
    sectorIes: str
    idCaracter: int
    caracterIes: str
    codigoDelDepartamentoIes: int
    departamentoDeDomicilioDeLaIes: str
    codigoDelMunicipioIes: int
    municipioDeDomicilioDeLaIes: str
    codigoSniesDelPrograma: int
    programaAcademico: str
    idNivelAcademico: int
    nivelAcademico: str
    idNivelDeFormacion: int
    nivelDeFormacion: str
    idMetodologia: int
    metodologia: str
    idArea: int
    areaDeConocimiento: str
    idNucleo: int
    nucleoBasicoDelConocimientoNbc: str
    idCineCampoAmplio: int
    descCineCampoAmplio: str
    idCineCampoEspecifico: int
    descCineCampoEspecifico: str
    idCineCodigoDetallado: int
    descCineCodigoDetallado: str
    codigoDelDepartamentoPrograma: int
    departamentoDeOfertaDelPrograma: str
    codigoDelMunicipioPrograma: int
    municipioDeOfertaDelPrograma: str

    def __init__(self):
        self.codigo_de_la_institucion = None
        self.ies_padre = None
        self.institucion_de_educacion_superior_ies = None
        self.principal_o_seccional = None
        self.id_sector_ies = None
        self.sector_ies = None
        self.id_caracter = None
        self.caracter_ies = None
        self.codigo_del_departamento_ies = None
        self.departamento_de_domicilio_de_la_ies = None
        self.codigo_del_municipio_ies = None
        self.municipio_de_domicilio_de_la_ies = None
        self.codigo_snies_del_programa = None
        self.programa_academico = None
        self.id_nivel_academico = None
        self.nivel_academico = None
        self.id_nivel_de_formacion = None
        self.nivel_de_formacion = None
        self.id_metodologia = None
        self.metodologia = None
        self.id_area = None
        self.area_de_conocimiento = None
        self.id_nucleo = None
        self.nucleo_basico_del_conocimiento_nbc = None
        self.id_cine_campo_amplio = None
        self.desc_cine_campo_amplio = None
        self.id_cine_campo_especifico = None
        self.desc_cine_campo_especifico = None
        self.id_cine_codigo_detallado = None
        self.desc_cine_codigo_detallado = None
        self.codigo_del_departamento_programa = None
        self.departamento_de_oferta_del_programa = None
        self.codigo_del_municipio_programa = None
        self.municipio_de_oferta_del_programa = None
        self.consolidados = {}  # Diccionario para almacenar objetos Consolidado

        # Métodos de asignación (Setters)
    def set_codigo_de_la_institucion(self, valor): self.codigo_de_la_institucion = valor
    def set_ies_padre(self, valor): self.ies_padre = valor
    def set_institucion_de_educacion_superior_ies(self, valor): self.institucion_de_educacion_superior_ies = valor
    def set_principal_o_seccional(self, valor): self.principal_o_seccional = valor
    def set_id_sector_ies(self, valor): self.id_sector_ies = valor
    def set_sector_ies(self, valor): self.sector_ies = valor
    def set_id_caracter(self, valor): self.id_caracter = valor
    def set_caracter_ies(self, valor): self.caracter_ies = valor
    def set_codigo_del_departamento_ies(self, valor): self.codigo_del_departamento_ies = valor
    def set_departamento_de_domicilio_de_la_ies(self, valor): self.departamento_de_domicilio_de_la_ies = valor
    def set_codigo_del_municipio_ies(self, valor): self.codigo_del_municipio_ies = valor
    def set_municipio_de_domicilio_de_la_ies(self, valor): self.municipio_de_domicilio_de_la_ies = valor
    def set_codigo_snies_del_programa(self, valor): self.codigo_snies_del_programa = valor
    def set_programa_academico(self, valor): self.programa_academico = valor
    def set_id_nivel_academico(self, valor): self.id_nivel_academico = valor
    def set_nivel_academico(self, valor): self.nivel_academico = valor
    def set_id_nivel_de_formacion(self, valor): self.id_nivel_de_formacion = valor
    def set_nivel_de_formacion(self, valor): self.nivel_de_formacion = valor
    def set_id_metodologia(self, valor): self.id_metodologia = valor
    def set_metodologia(self, valor): self.metodologia = valor
    def set_id_area(self, valor): self.id_area = valor
    def set_area_de_conocimiento(self, valor): self.area_de_conocimiento = valor
    def set_id_nucleo(self, valor): self.id_nucleo = valor
    def set_nucleo_basico_del_conocimiento_nbc(self, valor): self.nucleo_basico_del_conocimiento_nbc = valor
    def set_id_cine_campo_amplio(self, valor): self.id_cine_campo_amplio = valor
    def set_desc_cine_campo_amplio(self, valor): self.desc_cine_campo_amplio = valor
    def set_id_cine_campo_especifico(self, valor): self.id_cine_campo_especifico = valor
    def set_desc_cine_campo_especifico(self, valor): self.desc_cine_campo_especifico = valor
    def set_id_cine_codigo_detallado(self, valor): self.id_cine_codigo_detallado = valor
    def set_desc_cine_codigo_detallado(self, valor): self.desc_cine_codigo_detallado = valor
    def set_codigo_del_departamento_programa(self, valor): self.codigo_del_departamento_programa = valor
    def set_departamento_de_oferta_del_programa(self, valor): self.departamento_de_oferta_del_programa = valor
    def set_codigo_del_municipio_programa(self, valor): self.codigo_del_municipio_programa = valor
    def set_municipio_de_oferta_del_programa(self, valor): self.municipio_de_oferta_del_programa = valor
    def set_consolidado(self, consolidado, index): self.consolidados[index] = consolidado

    # Métodos de obtención (Getters)
    def get_codigo_de_la_institucion(self): return self.codigo_de_la_institucion
    def get_ies_padre(self): return self.ies_padre
    def get_institucion_de_educacion_superior_ies(self): return self.institucion_de_educacion_superior_ies
    def get_principal_o_seccional(self): return self.principal_o_seccional
    def get_id_sector_ies(self): return self.id_sector_ies
    def get_sector_ies(self): return self.sector_ies
    def get_id_caracter(self): return self.id_caracter
    def get_caracter_ies(self): return self.caracter_ies
    def get_codigo_del_departamento_ies(self): return self.codigo_del_departamento_ies
    def get_departamento_de_domicilio_de_la_ies(self): return self.departamento_de_domicilio_de_la_ies
    def get_codigo_del_municipio_ies(self): return self.codigo_del_municipio_ies
    def get_municipio_de_domicilio_de_la_ies(self): return self.municipio_de_domicilio_de_la_ies
    def get_codigo_snies_del_programa(self): return self.codigo_snies_del_programa
    def get_programa_academico(self): return self.programa_academico
    def get_id_nivel_academico(self): return self.id_nivel_academico
    def get_nivel_academico(self): return self.nivel_academico
    def get_id_nivel_de_formacion(self): return self.id_nivel_de_formacion
    def get_nivel_de_formacion(self): return self.nivel_de_formacion
    def get_id_metodologia(self): return self.id_metodologia
    def get_metodologia(self): return self.metodologia
    def get_id_area(self): return self.id_area
    def get_area_de_conocimiento(self): return self.area_de_conocimiento
    def get_id_nucleo(self): return self.id_nucleo
    def get_nucleo_basico_del_conocimiento_nbc(self): return self.nucleo_basico_del_conocimiento_nbc
    def get_id_cine_campo_amplio(self): return self.id_cine_campo_amplio
    def get_desc_cine_campo_amplio(self): return self.desc_cine_campo_amplio
    def get_id_cine_campo_especifico(self): return self.id_cine_campo_especifico
    def get_desc_cine_campo_especifico(self): return self.desc_cine_campo_especifico
    def get_id_cine_codigo_detallado(self): return self.id_cine_codigo_detallado
    def get_desc_cine_codigo_detallado(self): return self.desc_cine_codigo_detallado
    def get_codigo_del_departamento_programa(self): return self.codigo_del_departamento_programa
    def get_departamento_de_oferta_del_programa(self): return self.departamento_de_oferta_del_programa
    def get_codigo_del_municipio_programa(self): return self.codigo_del_municipio_programa
    def get_municipio_de_oferta_del_programa(self): return self.municipio_de_oferta_del_programa
    def get_consolidado(self, numero_indicativo_sexo_semestre): return self.consolidados[numero_indicativo_sexo_semestre]

