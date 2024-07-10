

class TestHealthCheck():
    def test_healthcheck(self, healthcheck):
        
        healthcheck
        
        assert healthcheck.status_code == 200
        assert healthcheck.json()['topic'] == "orders_api__health_check"
        assert 'partition' and \
                'offset' and \
                'leaderEpoch' and \
                'topicPartition' in healthcheck.json()
