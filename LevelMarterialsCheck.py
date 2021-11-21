import unreal


def try_cast(object_to_cast, object_class):
    try:
        return object_class.cast(object_to_cast)
    except:
        return None


editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
components = unreal.EditorActorSubsystem.get_all_level_actors_components(editor_actor_subsystem)

unfiltered_materials = []
Materials = []

for comp in components:
    mesh_component = try_cast(comp, unreal.MeshComponent)
    if mesh_component is not None:
        unfiltered_materials.extend(mesh_component.get_materials())

set_mat = set(unfiltered_materials)

for mat in set_mat:
    quantity = unfiltered_materials.count(mat)
    stats = unreal.MaterialEditingLibrary.get_statistics(mat)
    Materials.append([mat, stats, quantity])


print("{:<30} {:<15} {:<15} {:<10} {:<5}".format('Name', 'Instructions', 'TextureSamples', 'Samplers', 'Quantity'))

for mat in Materials:
    name = mat[0].get_name()
    vertex_instructions = mat[1].num_vertex_shader_instructions
    pixel_instructions = mat[1].num_pixel_shader_instructions
    vert_texture_samples = mat[1].num_vertex_texture_samples
    pix_texture_samples = mat[1].num_pixel_texture_samples
    samplers = mat[1].num_samplers
    quantity = mat[2]
    instr = "v({0}):p({1})".format(vertex_instructions, pixel_instructions)
    texture_samples = "v({0}):p({1})".format(vert_texture_samples, pix_texture_samples)
    print("{:<30} {:<15} {:<15} {:<10} {:<5}".format(name, instr, texture_samples, samplers, quantity))
