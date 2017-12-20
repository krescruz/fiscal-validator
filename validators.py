"""
Validators python for fiscal data in México

CURP - Clave Única de Registro de Población
RFC - Registro Federal de Contribuyentes
NSS - Número de Seguro Social

Repository url https://github.com/krescruz/fiscal-validator
"""
import re


def rfc_validator(value):
    message = 'Registro Federal de Contribuyentes invalido'
    regex = r'^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$'

    if not re.match(regex, value):
        raise ValueError(message)


def nss_validator(value):
    message = 'Número de Seguro Social invalido'
    regex = '^(\d{2})(\d{2})(\d{2})\d{5}$'

    if not re.match(regex, value):
        raise ValueError()


def curp_validator(value):
    message = 'Clave Única de Registro de Población invalido'
    regex = r'^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$'

    if not re.match(regex, value):
        raise ValueError(message)
