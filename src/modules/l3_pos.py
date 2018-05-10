#!/usr/bin/env python3

def POS_finder(pos_from_treetagger, lemme):
    pos = 'classe_inconnue'

##########
# FR
    if "VER" in pos_from_treetagger :
        if ("être" in lemme) :
            pos = 'verbe_etre' 
            
        elif ("valoir" in lemme) or ("diminuer" in lemme) or ("augmenter" in lemme) \
        or ("doubler" in lemme) or ("tripler" in lemme) or ("quadrupler" in lemme) :
            pos = 'verbe_comp' 
        else :
            pos = 'verbe'
            
    if "ADJ" in pos_from_treetagger :
        pos = 'adjectif'
    if "ADV" in pos_from_treetagger :
        if ("plus") in lemme or ("moins" in lemme) or ("aussi" in lemme) :
            pos = 'adverbe_comp' 
        else :
            pos = 'adverbe'

        
    if "DET" in pos_from_treetagger :
        if ("le" in lemme) or ("la" in lemme) or ("les" in lemme) :
            pos = 'le+' 
        else :
            pos = 'determinant'
    
    if "PRO" in pos_from_treetagger :
        # if ("que" in lemme) :
        #     pos = "que+"
        pos = 'pronom'

    if ("NOM" in pos_from_treetagger) or ("NAM" in pos_from_treetagger) :
        pos = 'nom'
    if "NUM" in pos_from_treetagger :
        pos = 'nombre'

    if "PRP" in pos_from_treetagger :
        if (lemme == "de") or (lemme == 'du') or (lemme == 'des') :
            pos = 'de+' 
        else :
            pos = 'preposition'
        
    if "PUN" in pos_from_treetagger :
        pos = 'ponctuation'
        
    if "KON" in pos_from_treetagger :
        if ("que" in lemme) :
            pos = "que+"
        else :
            pos = 'conjonction'
                
    if "SENT" in pos_from_treetagger :
        pos = 'ponctuation'
    
        
##########
# EN

    return str(pos)
