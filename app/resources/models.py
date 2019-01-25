from app import db

class tbl_charge(db.Model):
    Min = db.Column(db.Integer(64))
    Max= db.Column(db.Integer(64))   
    Withdraw_charge= db.Column(db.Integer(64)) 
    Send_to_unregistered_user= db.Column(db.Integer(64)) 
    Send_to_registered_user= db.Column(db.Integer(64)) 
    

    def __repr__(self):
        return '<tbl_charge {}>'.format(self.Min)   

class tbl_business_account(db.Model):
    uuid = db.Column(db.Integer, primary_key=True)
    account_no = db.Column(db.Integer(64))
    account_name = db.Column(db.String(64))
    status = db.Column(db.String(64))
    account_balance = db.Column(db.Integer(64))
    last_activity = db.Column(DateTime, default=datetime.datetime.utcnow)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<tbl_business_account {}>'.format(self.uuid)

class tbl_main_transaction(db.Model):
    uuid = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('tbl_business_account.uuid'))
    receipt = db.Column(db.String(120), unique=True)
    party_a = db.Column(db.Integer(120))
    party_b = db.Column(db.Integer(120))
    amount = db.Column(db.Integer(120))
    amount_type = db.Column(db.String(120))
    transaction_type = db.Column(db.String(120))
    

    def __repr__(self):
        return '<tbl_main_transaction {}>'.format(self.uuid)

class tbl_subtransaction(db.Model):
    uuid = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('tbl_business_account.uuid'))
    receipt = db.Column(db.String(120), unique=True)
    phone = db.Column(db.Integer(120))
    amount = db.Column(db.Integer(120))
    amount_type = db.Column(db.String(120))
    transaction_type = db.Column(db.String(120))


    def __repr__(self):
        return '<tbl_subtransaction {}>'.format(self.phone) 

class tbl_mobile_wallet_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sur_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    reg_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    account_bal = db.Column(db.Integer(120))
    status = db.Column(db.String(120))
    last_activity = db.Column(DateTime, default=datetime.datetime.utcnow)
    phone_number = db.Column(db.Integer(120), unique=True)
    pin = db.Column(db.String(128))

    def __repr__(self):
        return '<tbl_mobile_wallet_detail {}>'.format(self.sur_name) 

class tbl_customer_detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sur_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    second_name = db.Column(db.String(64))
    id_number = db.Column(db.String(120),unique=True)
    phone_number = db.Column(db.String(120) unique=True)
    reg_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(120))

    

    def __repr__(self):
        return '<tbl_customer_detail {}>'.format(self.id_number) 