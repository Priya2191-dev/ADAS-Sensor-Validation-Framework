def sensor_fusion(camera, radar):
    return [(c + r)/2 for c, r in zip(camera, radar)]
