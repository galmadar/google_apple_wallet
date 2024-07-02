import hashlib
import json
import os

def generate_manifest(directory):
    manifest = {}
    for filename in os.listdir(directory):
        if filename == 'manifest.json' or filename == 'signature':
            continue
        filepath = os.path.join(directory, filename)
        with open(filepath, 'rb') as f:
            file_hash = hashlib.sha1(f.read()).hexdigest()
            manifest[filename] = file_hash
    return manifest

def write_manifest(directory, manifest):
    manifest_path = os.path.join(directory, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=4)

pass_directory = 'source directory'
manifest = generate_manifest(pass_directory)
write_manifest(pass_directory, manifest)

