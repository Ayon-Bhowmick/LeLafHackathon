import boto3
import sagemaker
from sagemaker import get_execution_role

role = get_execution_role()
sess = sagemaker.Session()
bucket = sess.default_bucket()
prefix = 'ic-transfer-learning'

region = sess.boto_region_name
image_name = sagemaker.image_uris.retrieve(region=boto3.Session().region_name, framework='image-classification')


