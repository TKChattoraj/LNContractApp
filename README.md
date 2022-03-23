# LNContractApp
Contract Application on top of LN

Basic idea--model various business contracts.  Start with a promissory note.

Each contract counterparty runs the LNContractApp.

1.  Each party connects their app to their LN node.  Using Polar for now.
2.  Each party needs a way to communicate with counterparty.
    a.  set up separate servers for each party using gRPC.
    b.  Is there a way to communicate solely through the LN nodes?  Need to understand options
3.  Each party might need limited access to the counterparty's LN node.  
4.  App will manage contract
    a.  cryptographically sign the contract.
    b.  prompt and/or automatically send payments via LN.
5.  GUI
    a.  maybe use PyQt?  

Contract Object:
-party
-counterparty
-party_obligation = [ consieration objects]
-counterparty_obligation = [consideration objects]
-contract text
-signatures

Consideration Object:
-type:  goods, service, payment
-due_date