import './App.css';
import { useState, useEffect } from 'react';
import GeneList from './components/genelist';
import GraphView from './components/graph';
import Modal from './components/modal';
// import {useReadCypher} from 'use-neo4j';
// import {useAxiosPrivate} from 'axios';


function App() {
  // const [numEntries, setNumEntries] = useState(10);
  const [showModal, setShowModal] = useState(false);
  const [graphData, setGraphData] = useState([{name: "AIDS"}, {name: "soham's left nut"}, {name: "soham's right nut"}]);

  const handleModalData = (data) => {
    setGraphData(data)
    // console.log(data)

  }


  // useEffect(() => {
  //   fetch("/data").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       console.log(data)
  //       setData(data)
  //     }
  //   ).catch(
  //     error => console.error("Error fetching data: ", error)
  //   )
  // }, [])



  return (
    <div class="z-0">
      <div className="App" class="flex justify-between items-center bg-gray-600 p-3 text-neutral-50 text-lg">
        <p>
          Predicting Gene Mutations Using Convolutional Neural Networks for Neurodegenerative Diseases
        </p>
        <div 
          onClick={() => setShowModal(!showModal)}
          class="
            p-2 
            text-sm 
            rounded-xl 
            w-30 
            bg-blue-500 
            hover:bg-blue-400 
            cursor-pointer
          ">
          Options 
        </div> 
      </div>
      
      <div class="flex text-black">
        <GeneList list={graphData}/>
        <GraphView graph_data={graphData}/>
      </div>
 
      {(showModal && <Modal isOpen={showModal} onClose={() => setShowModal(false)} handleModalData={handleModalData}/>)}
    </div>
  );
}

export default App;
