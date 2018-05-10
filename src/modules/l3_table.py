#!/usr/bin/env python3

def tell_sujet_logique():
    print("== Nous sommes dans 'sujet_logique' ==")
    
def tell_se():
    print("== Nous sommes au coeur d'une structure avec être.\n" \
    "Il me faut avancer pour plus de détails. ==")

def tell_sc():
    print("== Nous sommes au coeur de 'structure_comparative' ==")

def tell_scv():
    print("== On valide la 'structure_comparative' ==")

def tell_ss():
    print("== Nous sommes au coeur de 'structure_superlative' ==")

def tell_ssv():
    print("== On valide la 'structure_superlative' ==")

def tell_fin():
    print("== Nous sommes à la fin de la phrase ==")

#GEN table
# import itertools
# a = ['pronom', 'nom', 'determinant', 'adjectif', 'adverbe', 'verbe', 'preposition', 'conjonction']
# b = ['pronom', 'nom', 'determinant', 'adjectif', 'adverbe', 'verbe', 'preposition', 'conjonction']
# for i in itertools.product(a , b) :
#   print(str(i) + ' : (\'\' , \'\'),' )  

table_de_transition = {

    ############################
    # INIT
    ('r_init', 'pronom') : ('sujet_logique', tell_sujet_logique), 
    ('r_init', 'nom') : ('sujet_logique' , tell_sujet_logique), 
    ('r_init', 'determinant') : ('sujet_logique' , tell_sujet_logique), 

    ############################
    # sujet_logique
    ('sujet_logique', 'pronom') : ('sujet_logique' , tell_sujet_logique), 
    ('sujet_logique', 'nom') : ('sujet_logique' , tell_sujet_logique), 
    ('sujet_logique', 'determinant') : ('sujet_logique' , tell_sujet_logique), 
    ('sujet_logique', 'le+') : ('sujet_logique' , tell_sujet_logique), 
    
    ('sujet_logique', 'verbe') : ('sujet_logique' , tell_sujet_logique),
    ('sujet_logique', 'verbe_etre') : ('structure_avec_etre' , tell_se),
    ('sujet_logique', 'verbe_comp') : ('structure_comparative_valide' , tell_scv),
    
    ############################
    # STRUCTURE avec ETRE
    
    ('structure_avec_etre' , 'adverbe_comp') : ('structure_comparative' , tell_sc), 
    
    ('structure_avec_etre' , 'adjectif') : ('structure_comparative' , tell_sc), 
    
    ('structure_avec_etre' , 'le+') : ('structure_superlative' , tell_ss),
    
    ############################
    # STRUCTURE COMPARATIVE (est (moins|plus|aussi) ...? )

    ('structure_comparative', 'adverbe') : ('structure_comparative_valide' , tell_scv),
    ('structure_comparative', 'adjectif') : ('structure_comparative_valide' , tell_scv),

    ('structure_comparative', 'pronom') : ('structure_comparative_valide' , tell_scv),
    ('structure_comparative', 'nom') : ('structure_comparative_valide' , tell_scv),
    ('structure_comparative', 'nombre') : ('structure_comparative_valide' , tell_scv),
    
    ('structure_comparative_valide', 'conjonction') : ('structure_comparative' , tell_sc),
    ('structure_comparative_valide', 'que+') : ('structure_comparative' , tell_sc),
    ('structure_comparative_valide', 'preposition') : ('structure_comparative' , tell_sc),
    ('structure_comparative_valide', 'le+') : ('structure_comparative' , tell_sc),
    ('structure_comparative_valide', 'de+') : ('structure_comparative' , tell_sc),

    ('structure_comparative', 'que+') : ('structure_comparative' , tell_sc),

    ('structure_comparative_valide', 'ponctuation') : ('fin_de_phrase' , tell_fin),
    
    ############################
    # STRUCTURE SUPERLATIVE (est le (moins|plus) (adj|adv) ...? )

    ('structure_superlative' , 'adverbe_comp') : ('structure_superlative' , tell_ss),

    ('structure_superlative' , 'adjectif') : ('structure_superlative_valide' , tell_ssv),
    ('structure_superlative' , 'adverbe') : ('structure_superlative_valide' , tell_ssv),
    ('structure_superlative' , 'nombre') : ('structure_superlative_valide' , tell_ssv),
    ('structure_superlative' , 'nom') : ('structure_superlative_valide' , tell_ssv),
    ('structure_superlative' , 'pronom') : ('structure_superlative_valide' , tell_ssv),
        
    ('structure_superlative_valide' , 'nom') : ('structure_superlative_valide' , tell_ssv),
    
    ('structure_superlative_valide' , 'de+') : ('structure_superlative' , tell_ss),
        
    ('structure_superlative_valide' , 'ponctuation') : ('fin_de_phrase' , tell_fin),
    
    ############################
}
