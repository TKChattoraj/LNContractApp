#
# contains the methods use to instantiate objects corresponding to db tables
# it creates and populates models, conditions the data into a form usable to 
# create instantiate object related to db tables, but usable.
# 


from LNContract_classes import  Contract, Entity, LnNode, KCommServer, KText
from db_methods import get_model

def set_up_contract_object(chosen_k_no, contract_record, party_id, counterparty_id, description, status):
        # create the party and counterparty objects/models
        party=set_up_entity_object(party_id)
        counterparty=set_up_entity_object(counterparty_id)

        contract_id=contract_record.value("id")
        contract_texts=get_ktexts(contract_id)
        print("contract texts:")
        print(contract_texts)
       
        # create the contract model object
        contract=Contract(contract_id, chosen_k_no, party, counterparty, contract_texts, description, status)
        return contract


def set_up_entity_object(entity_id):

    ##### create the party object:

    entity_model=get_model("entities")
    where_phrase="id={}".format(entity_id)
    entity_model.setFilter(where_phrase)
    entity_model.select()
    entity_record=entity_model.record(0)

    #### create the party's ln_node object:

    # select the ln_node record

    entity_ln_node_id=entity_record.value("ln_node_id")

    print("within entity setutp")
    print(entity_ln_node_id)
    

    # create the LnNode object:
    ln_node=set_up_ln_node_object(entity_ln_node_id)

    # create the kcomm_server object:
    # select the kcomm record
    entity_kcomm_id=entity_record.value("kcomm_server_id")
    
    ### create the party's kcomm_server object:
    kcomm_server=set_up_kcomm_object(entity_kcomm_id)
    
    # create the party object:
    id=entity_record.value("id")
    name=entity_record.value("name")
    ln_node= ln_node
    kcomm=kcomm_server
    entity=Entity(id, name, ln_node, kcomm)  
    return entity
    
def set_up_ln_node_object(ln_node_id):
    ln_node_model=get_model("ln_nodes")
    where_phrase="id={}".format(ln_node_id)
    ln_node_model.setFilter(where_phrase)
    ln_node_model.select()
    ln_node_record=ln_node_model.record(0)
    
    ln_id= ln_node_record.value("id")
    ln_address= ln_node_record.value("address")
    ln_tls_path=ln_node_record.value("tls_path")
    ln_macaroon_path=ln_node_record.value("macaroon_path")
    ln_status=ln_node_record.value("status")

    # create the actual LnNode object:
    ln_node=LnNode(
        ln_id,
        ln_address,
        ln_tls_path,
        ln_macaroon_path,
        ln_status
    )
    return ln_node

def set_up_kcomm_object(kcomm_id ):
    #  Need to think about abstracting the creation of these models into objects.
    #  Also need to think about how to make less fragile in case of a database change.
    #  That would require obtaining the values based on the specific column names for the table
    #  And so need to think about the use of the "columns" variable in the get_model() function.

    
    kcomm_model=get_model("kcomm_servers")
    where_phrase="id={}".format(kcomm_id)
    kcomm_model.setFilter(where_phrase)
    kcomm_model.select()
    kcomm_record=kcomm_model.record(0)
    
    k_id=kcomm_record.value("id")
    k_address=kcomm_record.value("address")
    k_tls_cert=kcomm_record.value("tls_cert")
    k_status=kcomm_record.value("status")

    # create the actual KCommServer object
    kcomm_server=KCommServer(
        k_id,
        k_address,
        k_tls_cert,
        k_status
    )
    return kcomm_server

def get_ktexts(k_id):
    # use the id_val to get the contract text to display
    k_text_model=get_model("ktexts")
    where_clause="contract_id={}".format(k_id)
    k_text_model.setFilter(where_clause)
    k_text_model.select()
    rows=k_text_model.rowCount()
    k_text_list=[]
    for i in range(rows):
        record=k_text_model.record(i)
        id=record.value("id")
        filename=record.value("filename")
        contract_id=record.value("contract_id")
        status=record.value("satus")
        ktext=KText(id, filename, contract_id, status)
        k_text_list.append(ktext)
    return k_text_list