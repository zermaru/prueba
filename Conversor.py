# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:19:04 2022

@author: User
"""

def val(eva: float) -> bool:
    '''
    Esta función evalua el valor de la moneda a la que se quier convertir
    el valor del dinero, si la monedaa la que se convierte vale más o 
    menos que la moneda actual

    Parameters
    ----------
    eva : float
        DESCRIPTION. Es el valor de la moneda a la que se quiere convertir

    Returns
    -------
    bool
        DESCRIPTION.

    '''
    if eva > 1:
        
        div = True
        
    else:
        
        div = False
        
    return div


class Conversor():
    '''
    Esta clase hace una conversión de diferentes monedas

    '''

    def __init__(self, valor: float) -> None:
        '''
        Esta función inicializa los parametros de la clase

        Parameters
        ----------
        valor : float
            DESCRIPTION. ES el dinero que se quiere convertir

        Returns
        -------
        None
            DESCRIPTION.

        '''

        self.valor = valor
  
    def conver(self, valor_moneda : float, nombre_moneda : str) -> float:  
        '''
        Esta fución convierte de la moneda actual a la que se quiere convertir

        Parameters
        ----------
        valor_moneda : float
            DESCRIPTION. Es el valor de la moneda a la que se va a convertir
        nombre_moneda : str
            DESCRIPTION. Es el  nombre de la moneda a la que se va a convertir

        Returns
        -------
        float
            DESCRIPTION. Es el valor convertido del dinero

        '''
        div_c = val(eva=valor_moneda)   
        
        if div_c:  
            
            conver = self.valor / valor_moneda
            
        else:  
            
                conver = self.valor * valor_moneda
                
        print (f"El cambio a {nombre_moneda} es: {conver}")
        
        return conver
