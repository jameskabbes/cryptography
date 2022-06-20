import kabbes_cryptography as kcryp
import dir_ops as do

storage_Dir = do.Dir( do.get_cwd() ).join_Dir( path = 'CombinedEncryption' )
if not storage_Dir.exists():
    storage_Dir.create( override = True )

Combined_inst = kcryp.Combined( Dir = storage_Dir )

private_Key_Path = do.Path( 'privatekey' )
public_Key_Path = do.Path( 'publickey' )

if not private_Key_Path.exists() or not public_Key_Path.exists():
    RSA_inst = kcryp.RSA()
    RSA_inst.get_new_Keys( set = True )

    if private_Key_Path.exists():
        private_Key_Path.remove( override = True )
    RSA_inst.export_private_Key( private_Key_Path )

    if public_Key_Path.exists():
        public_Key_Path.remove( override = True )
    RSA_inst.export_public_Key( public_Key_Path )
  

Combined_inst.RSA.import_private_Key( private_Key_Path, set = True )
Combined_inst.RSA.import_public_Key( public_Key_Path, set = True )

if input( 'Type "yes" to encrypt a new message: ' ) == 'yes':
    message = input('Enter a message to encrypt: ')
    Combined_inst.encrypt( bytes(message, encoding = 'utf-8' ) )
    Combined_inst.Dir.list_contents_Paths().print_atts()

input('Press enter to decrypt')
Combined_inst.import_from_Dir()
dec_message = Combined_inst.decrypt().decode( encoding = 'utf-8' )

print (dec_message)