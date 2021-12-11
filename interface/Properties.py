import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty
from bpy.types import PropertyGroup


class MyProperties(PropertyGroup):
    # PATHS
    data_path: StringProperty(
        name="File Path",
        description="File path to .mov file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )
    # BUTTONS
    button_start_detection: StringProperty(
        name="",
        description="Detects features and record results in blender.",
        default="Start Tracking"
    )

    button_add_rig: StringProperty(
        name="",
        description="Adds an armature as target for detected results.",
        default="Add Driver Rig"
    )

    # ENUMS
    enum_detection_type: EnumProperty(
        name="",
        description="Select detection type for motion tracking.",
        items=(
            ("POSE", "Pose", ""),
            ("HOLISTIC", "Holistic", ""),
            ("FACE", "Face", ""),
            ("HAND", "Hands", "")
        )
    )

    enum_synchronize: EnumProperty(
        name="Update",
        description="Select detection update type.",
        items=(
            ("SYNC", "synchronous", ""),
            ("ASYNC", "asynchronous", "")
        )
    )

    # SLIDER
    webcam_input_device: IntProperty(
        name="Webcam Device Slot",
        description="Select Webcam device.",
        min=-1,
        max=11,
        default=1,
    )


def get_user():
    return bpy.context.scene.m_cgtinker_mediapipe
