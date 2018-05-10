#!/usr/bin/env python3

def write_sujet_logique(file):
    file.write("\n\t== Nous sommes dans 'sujet_logique' ==")

def write_sv(file):
    file.write("\n\t== Nous sommes au coeur d'une structure avec verbe.\n" \
    "Il me faut avancer pour plus de détails. ==")
    
def write_se(file):
    file.write("\n\t== Nous sommes au coeur d'une structure avec être.\n" \
    "Il me faut avancer pour plus de détails. ==")

def write_sc(file):
    file.write("\n\t== Nous sommes au coeur de 'structure_comparative' ==")

def write_scv(file):
    file.write("\n\t== On valide la 'structure_comparative' ==")

def write_ss(file):
    file.write("\n\t== Nous sommes au coeur de 'structure_superlative' ==")

def write_ssv(file):
    file.write("\n\t== On valide la 'structure_superlative' ==")

def write_fin(file):
    file.write("\n\t== Nous sommes à la fin de la phrase ==")

#GEN table
# import itertools
# a = ['pronom', 'nom', 'determinant', 'adjectif', 'adverbe', 'verbe', 'preposition', 'conjonction']
# b = ['pronom', 'nom', 'determinant', 'adjectif', 'adverbe', 'verbe', 'preposition', 'conjonction']
# for i in itertools.product(a , b) :
#   print(str(i) + ' : (\'\' , \'\'),' )  

table_de_transition = {

    ############################
    # INIT
    ('r_init', 'le+') : ('r_init' , write_sujet_logique), 

    ('r_init', 'pronom') : ('sujet_logique', write_sujet_logique), 
    ('r_init', 'nom') : ('sujet_logique' , write_sujet_logique), 
    ('r_init', 'determinant') : ('sujet_logique' , write_sujet_logique), 

    ############################
    # sujet_logique
    ('sujet_logique', 'pronom') : ('sujet_logique' , write_sujet_logique), 
    ('sujet_logique', 'nom') : ('sujet_logique' , write_sujet_logique), 
    ('sujet_logique', 'determinant') : ('sujet_logique' , write_sujet_logique), 
    ('sujet_logique', 'adjectif') : ('sujet_logique' , write_sujet_logique), 
    ('sujet_logique', 'le+') : ('sujet_logique' , write_sujet_logique), 
    ('sujet_logique', 'preposition') : ('sujet_logique' , write_sujet_logique), # Le vélo à Paul
    
    ('sujet_logique', 'verbe') : ('structure_avec_verbe' , write_sv),
    ('sujet_logique', 'verbe_etre') : ('structure_avec_etre' , write_se),
    ('sujet_logique', 'verbe_comp') : ('structure_comparative_valide' , write_scv),
    
    ############################
    # STRUCTURE avec VERBE
    
    ('structure_avec_verbe' , 'adverbe_comp') : ('structure_comparative' , write_sc),
    ('structure_avec_verbe' , 'verbe') : ('structure_comparative' , write_sc),
    
    ('structure_avec_verbe', 'verbe_comp') : ('structure_comparative_valide' , write_scv),
    ############################
    # STRUCTURE avec ETRE
    
    ('structure_avec_etre' , 'adverbe_comp') : ('structure_comparative' , write_sc), 
        # CAUTION
    ('structure_avec_etre' , 'adverbe') : ('structure_comparative' , write_sc), 
    
    ('structure_avec_etre' , 'adjectif') : ('structure_comparative' , write_sc), 
    
    ('structure_avec_etre' , 'le+') : ('structure_superlative' , write_ss),
    
        ############################
        # STRUCTURE COMPARATIVE (est (moins|plus|aussi) ...? )

    ('structure_comparative', 'adverbe') : ('structure_comparative_valide' , write_scv),
    ('structure_comparative', 'adjectif') : ('structure_comparative_valide' , write_scv),

    ('structure_comparative', 'pronom') : ('structure_comparative_valide' , write_scv),
    ('structure_comparative', 'nom') : ('structure_comparative_valide' , write_scv),
    ('structure_comparative', 'nombre') : ('structure_comparative_valide' , write_scv),
    ('structure_comparative', 'verbe') : ('structure_comparative_valide' , write_scv),
    
    ('structure_comparative', 'le+') : ('structure_comparative' , write_sc),
    ('structure_comparative', 'determinant') : ('structure_comparative' , write_sc),

    ('structure_comparative_valide', 'verbe') : ('structure_comparative_valide' , write_scv),
    ('structure_comparative_valide', 'conjonction') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'adverbe') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'adjectif') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'que+') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'preposition') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'le+') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'de+') : ('structure_comparative' , write_sc),
    ('structure_comparative_valide', 'pronom') : ('structure_comparative' , write_sc),
    ('structure_comparative', 'que+') : ('structure_comparative' , write_sc),

    ('structure_comparative_valide', 'ponctuation') : ('fin_de_phrase' , write_fin),
    
        ############################
        # STRUCTURE SUPERLATIVE (est le (moins|plus) (adj|adv) ...? )

    ('structure_superlative' , 'adverbe_comp') : ('structure_superlative' , write_ss),

    ('structure_superlative' , 'adjectif') : ('structure_superlative_valide' , write_ssv),
    ('structure_superlative' , 'adverbe') : ('structure_superlative_valide' , write_ssv),
    ('structure_superlative' , 'nombre') : ('structure_superlative_valide' , write_ssv),
    ('structure_superlative' , 'nom') : ('structure_superlative_valide' , write_ssv),
    ('structure_superlative' , 'pronom') : ('structure_superlative_valide' , write_ssv),
        
    ('structure_superlative_valide' , 'nom') : ('structure_superlative_valide' , write_ssv),
    ('structure_superlative_valide' , 'pronom') : ('structure_superlative_valide' , write_ssv),
    ('structure_superlative_valide' , 'nombre') : ('structure_superlative_valide' , write_ssv),
    
    ('structure_superlative_valide' , 'verbe') : ('structure_superlative_valide' , write_ssv),
    
    ('structure_superlative_valide' , 'de+') : ('structure_superlative' , write_ss),
    ('structure_superlative_valide', 'que+') : ('structure_superlative' , write_ss),  
    ('structure_superlative_valide' , 'ponctuation') : ('fin_de_phrase' , write_fin),
    
    ############################
}
