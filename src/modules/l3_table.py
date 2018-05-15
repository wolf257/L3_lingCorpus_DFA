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
    
    
def tell_sujet_logique():
    print("\n\t== Nous sommes dans 'sujet_logique' ==")

def tell_sv():
    print("\n\t== Nous sommes au coeur d'une structure avec verbe.\n" \
    "Il me faut avancer pour plus de détails. ==")
    
def tell_se():
    print("\n\t== Nous sommes au coeur d'une structure avec être.\n" \
    "Il me faut avancer pour plus de détails. ==")

def tell_sc():
    print("\n\t== Nous sommes au coeur de 'structure_comparative' ==")

def tell_scv():
    print("\n\t== On valide la 'structure_comparative' ==")

def tell_ss():
    print("\n\t== Nous sommes au coeur de 'structure_superlative' ==")

def tell_ssv():
    print("\n\t== On valide la 'structure_superlative' ==")

def tell_fin():
    print("\n\t== Nous sommes à la fin de la phrase ==")

#GEN table
# import itertools
# a = ['pronom', 'nom', 'determinant', 'adjectif', 'adverbe', 'verbe', 'preposition', 'conjonction']
# b = ['pronom', 'nom', 'determinant', 'adjectif', 'adverbe', 'verbe', 'preposition', 'conjonction']
# for i in itertools.product(a , b) :
#   print(str(i) + ' : (\'\' , \'\'),' )  

table_de_transition = {

    ############################
    # INIT
    ('r_init', 'le+') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('r_init', 'pronom') : ('sujet_logique', write_sujet_logique, tell_sujet_logique), 
    ('r_init', 'nom') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('r_init', 'determinant') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('r_init', 'adjectif') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('r_init', 'verbe') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    
    ############################
    # sujet_logique
    ('sujet_logique', 'pronom') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('sujet_logique', 'nom') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('sujet_logique', 'determinant') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('sujet_logique', 'adjectif') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('sujet_logique', 'le+') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), 
    ('sujet_logique', 'preposition') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique), # Le vélo à Paul
    ('sujet_logique', 'possessive_ending') : ('sujet_logique' , write_sujet_logique, tell_sujet_logique),
    
    
    ('sujet_logique', 'verbe') : ('structure_avec_verbe' , write_sv, tell_sv),
    ('sujet_logique', 'verbe_etre') : ('structure_avec_etre' , write_se, tell_se),
    ('sujet_logique', 'verbe_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    
    ('sujet_logique', 'adjectif_comparatif') : ('structure_comparative' , write_sc, tell_sc),
    ('sujet_logique', 'adverbe_superlatif') : ('structure_superlative' , write_ss, tell_ss),

    ############################
    # STRUCTURE avec VERBE
    
    ('structure_avec_verbe' , 'verbe') : ('structure_avec_verbe' , write_sv, tell_sv),
    ('structure_avec_verbe', 'verbe_etre') : ('structure_avec_etre' , write_se, tell_se),

    ('structure_avec_verbe' , 'nom') : ('structure_avec_verbe' , write_sv, tell_sv),
    ('structure_avec_verbe', 'determinant') : ('structure_avec_verbe' , write_sv, tell_sv),
    ('structure_avec_verbe', 'pronom') : ('structure_avec_verbe' , write_sv, tell_sv),    

    ('structure_avec_verbe', 'preposition') : ('structure_avec_verbe' , write_sv, tell_sv),
    

    ('structure_avec_verbe', 'adjectif') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_avec_verbe', 'le+') : ('structure_superlative' , write_ss, tell_ss),
    
    ('structure_avec_verbe', 'verbe_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_avec_verbe', 'adjectif_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_avec_verbe' , 'adverbe_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    
    
    ############################
    # STRUCTURE avec ETRE
    ('structure_avec_etre' , 'nom') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_avec_etre' , 'adverbe_comparatif') : ('structure_comparative' , write_sc, tell_sc), 
        # CAUTION

    ('structure_avec_etre' , 'adverbe') : ('structure_comparative' , write_sc, tell_sc), 
    ('structure_avec_etre' , 'adjectif') : ('structure_comparative' , write_sc, tell_sc), 


    ('structure_avec_etre' , 'adjectif_superlatif') : ('structure_superlative' , write_ss, tell_ss), 
    ('structure_avec_etre' , 'le+') : ('structure_superlative' , write_ss, tell_ss),
    
    ('structure_avec_etre' , 'adjectif_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),

        ############################
        # STRUCTURE COMPARATIVE (est (moins|plus|aussi) ...? )

    ('structure_comparative', 'que+') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'possessive_ending') : ('structure_comparative' , write_sc, tell_sc),

    ('structure_comparative', 'le+') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative', 'determinant') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative', 'preposition') : ('structure_comparative' , write_sc, tell_sc),
    
    ('structure_comparative', 'verbe_etre') : ('structure_comparative' , write_sc, tell_sc),
    
    ('structure_comparative', 'adverbe') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'adverbe_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'adverbe_superlatif') : ('structure_comparative_valide' , write_scv, tell_scv),

    ('structure_comparative', 'adjectif') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'adjectif_comparatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'adjectif_superlatif') : ('structure_comparative_valide' , write_scv, tell_scv),
    
    ('structure_comparative', 'pronom') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'nom') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'nombre') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative', 'verbe') : ('structure_comparative_valide' , write_scv, tell_scv),

            ### STRUCTURE COMPARATIVE VALIDE

    ('structure_comparative_valide', 'conjonction') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'adverbe') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'adverbe_comparatif') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'adjectif') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'que+') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'preposition') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'le+') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'de+') : ('structure_comparative' , write_sc, tell_sc),
    ('structure_comparative_valide', 'pronom') : ('structure_comparative' , write_sc, tell_sc),

    ('structure_comparative_valide', 'verbe') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative_valide', 'verbe_etre') : ('structure_comparative_valide' , write_scv, tell_scv),

    ('structure_comparative_valide', 'nom') : ('structure_comparative_valide' , write_scv, tell_scv),
    ('structure_comparative_valide', 'nombre') : ('structure_comparative_valide' , write_scv, tell_scv),
    
    ('structure_comparative_valide', 'ponctuation') : ('fin_de_phrase' , write_fin, tell_fin),
    
        ############################
        # STRUCTURE SUPERLATIVE (est le (moins|plus) (adj|adv) ...? )

    ('structure_superlative' , 'adverbe_comparatif') : ('structure_superlative' , write_ss, tell_ss),
    ('structure_superlative', 'le+') : ('structure_superlative' , write_ss, tell_ss),

    ('structure_superlative' , 'adverbe') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative', 'adverbe_comparatif') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative', 'adverbe_superlatif') : ('structure_superlative_valide' , write_ssv, tell_ssv),

    ('structure_superlative' , 'adjectif') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative', 'adjectif_comparatif') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative', 'adjectif_superlatif') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    
    ('structure_superlative' , 'nombre') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative' , 'nom') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative' , 'pronom') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative', 'determinant') : ('structure_superlative_valide' , write_ssv, tell_ssv),

                ### STRUCTURE SUPERLATIVE VALIDE

    ('structure_superlative_valide' , 'de+') : ('structure_superlative' , write_ss, tell_ss),
    ('structure_superlative_valide', 'que+') : ('structure_superlative' , write_ss, tell_ss),  
    
    ('structure_superlative_valide', 'preposition') : ('structure_superlative' , write_ss, tell_ss),
    ('structure_superlative_valide', 'verbe_etre') : ('structure_superlative' , write_ss, tell_ss),
    
    
    ('structure_superlative_valide' , 'nom') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative_valide' , 'pronom') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative_valide' , 'nombre') : ('structure_superlative_valide' , write_ssv, tell_ssv),

    ('structure_superlative_valide' , 'adverbe') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    ('structure_superlative_valide', 'adjectif') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    
    ('structure_superlative_valide' , 'verbe') : ('structure_superlative_valide' , write_ssv, tell_ssv),
    
    ('structure_superlative_valide' , 'ponctuation') : ('fin_de_phrase' , write_fin, tell_fin),
    
    ############################
}
