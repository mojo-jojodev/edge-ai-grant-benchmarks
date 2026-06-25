def validate_throughput(tps, target=15.0):
    assert tps >= target, f"Failed target: {tps} TPS < {target} TPS"
    print("Real-time conversational speeds verified on resource-constrained hardware.")
