from client import PromptTo3dCadStepSolidGeneratorClient

def main():
    client = PromptTo3dCadStepSolidGeneratorClient()
    res = client.generate_parametric_cad_model('NEMA 17 stepper motor mounting bracket with vibration dampening slots')
    print('Text-to-CAD Generator: ' + res['cad_generation_id'] + ' (Format: ' + res['format'] + ')')
    print('B-Rep Faces: ' + str(res['brep_faces_count']) + ' | Watertight Manifold: ' + str(res['manifold_watertight_verified']))
    print('Geometric Tolerance: ' + str(res['geometric_tolerance_microns']) + ' microns')
    print('STEP File URL: ' + res['step_solid_file_url'])

if __name__ == '__main__':
    main()
