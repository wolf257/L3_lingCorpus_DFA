#!/usr/bin/env python3

########################################################
# LIST FUNCTIONS IN MODULES
#
#	+ POS_finder_fr()
#	+ POS_finder_en()
#
########################################################

def POS_finder_fr(pos_from_treetagger, lemme):
    pos = 'classe_inconnue'

    if (lemme == "que") :
        pos = "que+"
    elif (lemme == "le") or (lemme == "la") or (lemme == "les") :
        pos = 'le+' 
    elif (lemme == "de") or (lemme == 'du') or (lemme == 'des') :
        pos = 'de+' 

    else :
        if pos_from_treetagger.startswith("VER") :
            if (lemme == "être") :
                pos = 'verbe_etre' 
            
            elif (lemme == "valoir") or (lemme == "diminuer") or (lemme == "augmenter") \
            or (lemme == "doubler") or (lemme == "tripler") or (lemme == "quadrupler") :
                pos = 'verbe_comparatif' 
            else :
                pos = 'verbe'
            
        if pos_from_treetagger == "ADJ" :
            pos = 'adjectif'
        
        if pos_from_treetagger == "ADV" :
            if (lemme == "plus") or (lemme == "moins") or (lemme == "aussi") or (lemme == 'autant'):
                pos = 'adverbe_comparatif' 
            else :
                pos = 'adverbe'

        if pos_from_treetagger.startswith("DET") :
            pos = 'determinant'
    
        if pos_from_treetagger.startswith("PRO") :
            pos = 'pronom'

        if (pos_from_treetagger == "NOM") or (pos_from_treetagger == "NAM") :
            pos = 'nom'
        if pos_from_treetagger == "NUM" :
            pos = 'nombre'

        if pos_from_treetagger.startswith("PRP") :
            pos = 'preposition'
        
        if pos_from_treetagger.startswith("PUN") :
            pos = 'ponctuation'
        
        if pos_from_treetagger == "KON" :
            pos = 'conjonction'
                
        if pos_from_treetagger == "SENT" :
            pos = 'ponctuation'

    return str(pos)

def POS_finder_en(pos_from_treetagger, lemme):
    pos = 'classe_inconnue'

    if (lemme == "than") :
        pos = "que+"
    elif (lemme == "the") :
        pos = 'le+' 
    elif (lemme == "de") or (lemme == 'du') or (lemme == 'des') :
        pos = 'de+' 

    else :
        if pos_from_treetagger.startswith('V') :
            if (lemme == 'be') :
                pos = 'verbe_etre' 
            
            elif (lemme == 'increase') or (lemme == 'decrease') or(lemme == 'a') or(lemme == 'b') :
                pos = 'verbe_comparatif'
                
            else :
                pos = 'verbe'
        
        # ADJECTIVE
        if pos_from_treetagger == 'JJ' :
            pos = 'adjectif'
        if pos_from_treetagger == 'JJR' :
            pos = 'adjectif_comparatif'
        if pos_from_treetagger == 'JJS' :
            pos = 'adjectif_superlatif'

        # ADVERB
        if pos_from_treetagger == "RB" :
            pos = 'adverbe'
        if pos_from_treetagger == "RBR" :
            pos = 'adverbe_comparatif'
        if pos_from_treetagger == "RBS" :
            pos = 'adverbe_superlatif'
            
        # DETERMINANT
        if (pos_from_treetagger == 'DT') or (pos_from_treetagger == 'WDT') or (pos_from_treetagger == 'PDT') :
            pos = 'determinant'
    
        if pos_from_treetagger.startswith("PP") :
            pos = 'pronom'

        if (pos_from_treetagger == 'NN') or (pos_from_treetagger == 'NNS') \
        or (pos_from_treetagger == 'NP') or (pos_from_treetagger == 'NPS')  :
            pos = 'nom'
        if  pos_from_treetagger == 'CD' :
            pos = 'nombre'

        if pos_from_treetagger.startswith('IN') :
            pos = 'preposition'
        
        if pos_from_treetagger == "PUN" :
            pos = 'ponctuation'
        
        if pos_from_treetagger == "KON" :
            pos = 'conjonction'
        
        if pos_from_treetagger == "POS" :
            pos = 'possessive_ending'
                
        if pos_from_treetagger == "SENT" :
            pos = 'ponctuation'

    return str(pos)
