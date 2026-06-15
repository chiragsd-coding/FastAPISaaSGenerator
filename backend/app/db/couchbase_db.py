
from couchbase.cluster import Cluster
def get_cluster(conn):
    return Cluster(conn)
