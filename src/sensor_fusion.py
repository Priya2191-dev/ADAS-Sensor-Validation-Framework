def sensor_fusion(camera, radar):
    """
    Fuse camera and radar data.
    """
    fused = []
    for c, r in zip(camera, radar):
        avg = (c + r) / 2
        fused.append(avg)

    return fused


if __name__ == "__main__":
    print(sensor_fusion([10], [20]))
