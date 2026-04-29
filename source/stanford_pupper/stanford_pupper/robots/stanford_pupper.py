# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause


import isaaclab.sim as sim_utils
from isaaclab.actuators import ActuatorNetMLPCfg, DCMotorCfg, ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.utils.assets import ISAAC_NUCLEUS_DIR, ISAACLAB_NUCLEUS_DIR
import os


ASSET_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))),
    "assets")
R_MULT = 0.0174533


##
# Configuration
##


PUPPER_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{ASSET_DIR}/stanford_pup.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False, solver_position_iteration_count=4, solver_velocity_iteration_count=1
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, .27),
        joint_pos={
            "LF_HIP_JOINT": 0.0,
            "LF_THIGH_JOINT": 0.0,
            "LF_THIGH_FOOT_JOINT": 0.0,
            "LH_HIP_JOINT": 0.0,
            "LH_THIGH_JOINT": 0.0,
            "LH_THIGH_FOOT_JOINT": 0.0,
            "RF_HIP_JOINT": 0.0,
            "RF_THIGH_JOINT": 0.0,
            "RF_THIGH_FOOT_JOINT": 0.0,
            "RH_HIP_JOINT": 0.0,
            "RH_THIGH_JOINT": 0.0,
            "RH_THIGH_FOOT_JOINT": 0.0,
        },
        joint_vel={".*": 0.0},
    ),
    soft_joint_pos_limit_factor=0.8,
    actuators={
        "base_legs": DCMotorCfg(
            joint_names_expr=[".*_HIP_JOINT", ".*_THIGH_JOINT", ".*_THIGH_FOOT_JOINT"],
            effort_limit=33.5,
            saturation_effort=33.5,
            velocity_limit=21.0,
            stiffness=25.0,
            damping=0.5,
            friction=0.0,
        ),
    },
)

