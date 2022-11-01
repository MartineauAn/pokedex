const container = document.querySelector("#pokemon") 
const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(50,window.innerWidth / window.innerHeight,1, 1000);
console.log(container)
const renderer = new THREE.WebGLRenderer({ alpha: true});
renderer.setClearColor( 0x000000, 0 );
renderer.setPixelRatio(container.devicePixelRatio);
renderer.setSize(container.offsetWidth, container.offsetHeight);
container.appendChild(renderer.domElement)
camera.position.set(0,1,1);
camera.lookAt(scene.position)

var loader = new GLTFLoader();
loader.load(
   chemin + "/objects/6.glb",
   function ( gltf ) {
        gltf.scene.rotateY(0.60);
        scene.add(gltf.scene);
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

    renderer.render(scene, camera);
}

animate();

