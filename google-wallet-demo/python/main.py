from demo_generic import DemoGeneric
from demo_loyalty import DemoLoyalty

# issuer_id=3388000000022343316
issuer_id=3388000000022350529

# Create a demo class instance
# Creates the authenticated HTTP client
# demo = DemoGeneric()
demo = DemoLoyalty()

# Create a pass class
demo.create_class(issuer_id=issuer_id,
                    class_suffix='DEMO_WITH_AHARON_AND_NATAN')

# # Update a pass class
# demo.update_class(issuer_id=issuer_id,
#                     class_suffix='class_suffix')

# # Patch a pass class
# demo.patch_class(issuer_id=issuer_id,
#                     class_suffix='loyaltyclass_1123')

# # Add a message to a pass class
# demo.add_class_message(issuer_id=issuer_id,
#                         class_suffix='loyaltyclass_1123',
#                         header='header',
#                         body='body')

# # Create a pass object
# demo.create_object(issuer_id=issuer_id,
#                     class_suffix='demo_generic_1',
#                     object_suffix='demo_generic_1_object_1')

# # Update a pass object
# demo.update_object(issuer_id=issuer_id,
#                     object_suffix='loyalty_class_object2')

# # Patch a pass object
# demo.patch_object(issuer_id=issuer_id,
#                     object_suffix='loyalty_class_object')

# # Add a message to a pass object
# demo.add_object_message(issuer_id=issuer_id,
#                         object_suffix='loyalty_class_object2',
#                         header='header',
#                         body='body')

# # Expire a pass object
# demo.expire_object(issuer_id=issuer_id,
#                     object_suffix='object_suffix')

# # Create an "Add to Google Wallet" link
# # that generates a new pass class and object
# demo.create_jwt_new_objects(issuer_id=issuer_id,
#                             class_suffix='NATAN_AND_AHARON_AND_GAL',
#                             object_suffix='PESTIGAL')

# # Create an "Add to Google Wallet" link
# # that references existing pass classes and objects
# demo.create_jwt_existing_objects(issuer_id=issuer_id)

# # Create pass objects in batch
# demo.batch_create_objects(issuer_id=issuer_id,
#                             class_suffix='class_suffix')
