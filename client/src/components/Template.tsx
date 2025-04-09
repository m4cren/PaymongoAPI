import { OrbitControls } from "@react-three/drei";
import Sphere from "../Sphere";
import { Canvas } from "@react-three/fiber";
import axios from "axios";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

const Template = () => {
    const handlePayment = async (price: number) => {
        const data_to_send = {
            price_to_pay: price,
        };
        try {
            const response = await axios.post(
                "http://192.168.1.33:8888/paymongo/payment",
                data_to_send,
            );

            const url = response.data.checkout_url;
            console.dir(response);

            if (url) {
                window.open(url, "_blank");
            }
        } catch (error) {
            console.log(error);
        }
    };
    return (
        <div className="h-screen w-full">
            <Canvas>
                <directionalLight position={[0, 5, 5]} />
                <ambientLight intensity={0.3} />
                <Sphere position={[10, 4, -3]} color={"red"} radius={2} />

                <Sphere position={[5, 0, -1]} color={"blue"} radius={2} />
                <Sphere position={[5, 0, -20]} color={"yellow"} radius={2} />

                <Sphere position={[4, -2, 5]} color={"green"} radius={2} />

                <Sphere position={[0, 4, 2]} color={"pink"} radius={2} />

                <Sphere position={[-4, -2, 2]} color={"orange"} radius={2} />
                <OrbitControls />
            </Canvas>
            <Router>
                <Routes>
                    <Route
                        path="/"
                        element={
                            <div className="fixed z-1 top-[35%] left-[30%] translate-x-[-50%] translate-y=[-50%] flex flex-col gap-4">
                                <div>
                                    <h1 className="text-white text-8xl">
                                        Pay Mongo
                                    </h1>
                                </div>

                                <h2 className="text-white text-2xl">
                                    API Testing
                                </h2>
                                <button
                                    onClick={() => handlePayment(299)}
                                    className="text-white border-1 border-white/10 rounded-2xl backdrop-blur-2xl cursor-pointer"
                                >
                                    Buy Now for 299
                                </button>
                                <button
                                    onClick={() => handlePayment(1299)}
                                    className="text-white border-1 border-white/10 rounded-2xl backdrop-blur-2xl cursor-pointer"
                                >
                                    Buy Now for 1299
                                </button>
                            </div>
                        }
                    />
                    <Route path="/paid" element={<h1>Success</h1>} />
                    <Route path="/unsuccesful" element={<h1>Failed</h1>} />
                </Routes>
            </Router>
        </div>
    );
};

export default Template;
