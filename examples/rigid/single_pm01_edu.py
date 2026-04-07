import argparse

import genesis as gs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vis", action="store_true", default=False)
    parser.add_argument("-c", "--cpu", action="store_true", default=False)
    args = parser.parse_args()

    ########################## init ##########################
    gs.init(backend=gs.metal)

    ########################## create a scene ##########################
    scene = gs.Scene(
        viewer_options=gs.options.ViewerOptions(
            camera_pos=(1.5, 0.0, 1.5),
            camera_lookat=(0.0, 0.0, 0.5),
            camera_fov=40,
        ),
        rigid_options=gs.options.RigidOptions(
            gravity=(0, 0, -9.81),
        ),
        show_viewer=args.vis,
    )

    ########################## entities ##########################
    plane = scene.add_entity(
        gs.morphs.Plane(),
    )
    pm01 = scene.add_entity(
        gs.morphs.MJCF(file="xml/pm01_edu/pm01_edu.xml"),
        visualize_contact=True,
    )

    ########################## build ##########################
    scene.build()

    print("PM01 EDU links:", pm01.links)
    print("PM01 EDU joints:", pm01.joints)

    for i in range(1000):
        scene.step()


if __name__ == "__main__":
    main()
