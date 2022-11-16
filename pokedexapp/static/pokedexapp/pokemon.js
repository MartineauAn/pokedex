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

