import bpy
from bpy.props import StringProperty, EnumProperty, IntProperty, BoolProperty
from bpy.types import PropertyGroup


class CgtProperties(PropertyGroup):
    # BUTTONS
    button_start_detection: StringProperty(
        name="",
        description="Detects features and record results in stored in the cgt_driver collection.",
        default="Start Detection"
    )

    button_transfer_animation: StringProperty(
        name="",
        description="Armature as target for detected results.",
        default="Transfer Animation"
    )

    experimental_feature_bool: BoolProperty(
        name="Experimental Leg Transfer",
        description="Experimental feature to transfer legs when transferring pose data",
        default=False
    )

    # custom ui prop search
    def armature_poll(self, object):
        return object.type == 'ARMATURE'

    selected_rig: bpy.props.PointerProperty(
        type=bpy.types.Object,
        description="Select an armature for animation transfer.",
        name="Armature",
        poll=armature_poll)

    selected_driver_collection: StringProperty(
        name="",
        description="Select a collection of Divers.",
        default="Drivers"
    )
    # ENUMS
    # ("HOLISTIC", "Holistic", ""),
    enum_detection_type: EnumProperty(
        name="Target",
        description="Select detection type for motion tracking.",
        items=(
            ("HAND", "Hands", ""),
            ("FACE", "Face", ""),
            ("POSE", "Pose", ""),
        )
    )

    video_enum_detection_type: EnumProperty(
        name="Target",
        description="Select detection type for motion tracking.",
        items=(
            ("HAND", "Hands", ""),
            ("FACE", "Face", ""),
            ("POSE", "Pose", ""),
        )
    )

    # # Integer Input
    # webcam_input_device: IntProperty(
    #     name="Webcam Device Slot",
    #     description="Select Webcam device.",
    #     min=0,
    #     max=4,
    #     default=0
    # )

    video_file: StringProperty(
        name="Video Path",
        description="File path to video file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

    key_frame_step: IntProperty(
        name="Key Step",
        description="Select keyframe step rate.",
        min=1,
        max=12,
        default=4
    )

    data_path: StringProperty(
        name="File Path",
        description="File path to .mov file.",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )


def get_user():
    return bpy.context.scene.m_cgtinker_mediapipe
