const container = document.querySelector("#pokemon") 
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(50,window.innerWidth / window.innerHeight,1, 1000);
console.log(container)
const renderer = new THREE.WebGLRenderer({ alpha: true});
renderer.setClearColor( 0x000000, 0 );
renderer.setPixelRatio(container.devicePixelRatio);
renderer.setSize(container.offsetWidth, container.offsetHeight);
container.appendChild(renderer.domElement)
camera.position.set(-1.562983928520932,2.220798424732542,5.122226754040644);
//camera.lookAt(scene.position)
/* Helpers */
const gridHelper = new THREE.GridHelper(200, 50);
scene.add(gridHelper);
var loader = new GLTFLoader();
loader.load( 
   chemin + "/objects/6.glb",
   function ( gltf ) {

        const pokemon = gltf.scene;
        scene.add(pokemon);
       
        let vFoV = camera.getEffectiveFOV();
        let hFoV = camera.fov * camera.aspect;

        let FoV = Math.min(vFoV, hFoV);
        let FoV2 = FoV / 2;

        let dir = new THREE.Vector3();
        camera.getWorldDirection(dir);

        let bb = pokemon.geometry.boundingBox;
        let bs = pokemon.geometry.boundingSphere;
        let bsWorld = bs.center.clone();
        pokemon.localToWorld(bsWorld);

        let th = FoV2 * Math.PI / 180.0;
        let sina = Math.sin(th);
        let R = bs.radius;
        let FL = R / sina;

        let cameraDir = new THREE.Vector3();
        camera.getWorldDirection(cameraDir);

        let cameraOffs = cameraDir.clone();
        cameraOffs.multiplyScalar(-FL);
        let newCameraPos = bsWorld.clone().add(cameraOffs);

        camera.position.copy(newCameraPos);
        camera.lookAt(bsWorld);
        controls.target.copy(bsWorld);

        controls.update();

   },
);

const pointLight = new THREE.PointLight(0xffffff);
pointLight.position.set(5,5,5);

const ambientLight = new THREE.AmbientLight(0xffffff);
scene.add(pointLight,ambientLight);


const controls = new OrbitControls(camera, renderer.domElement);

function animate(){
    requestAnimationFrame(animate);
    controls.update();
    //console.log(controls.object.position)
    renderer.render(scene, camera);
}

animate();

