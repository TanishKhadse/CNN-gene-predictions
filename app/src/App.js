import './App.css';
import { useState, useEffect } from 'react';
import GeneList from './components/genelist';
import GraphView from './components/graph';
import Modal from './components/modal';
// import {useReadCypher} from 'use-neo4j';
// import {useAxiosPrivate} from 'axios';


function App() {
  const [numEntries, setNumEntries] = useState(10);
  const [showModal, setShowModal] = useState(false);
  const [geneData, setGeneData] = useState();
  const [data, setData] = useState([{}]); // testing RESTAPI

  useEffect(() => {
    fetch("/bio_data").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data.bio_data)
      }
    ).catch(
      error => console.error("Error fetching data: ", error)
    )
  }, [])

  // const axiosPrivate = useAxiosPrivate();

  // const {cypher, error, loading, first }  = useReadCypher(""); // query goes inside of quotes


  // const fetchGeneData = async () => {
  //   const response = await axiosPrivate.get(''); // put in api path
  //   const cData = response.data;
  //   setGeneData=(cData);
  // }


/**
 * API needs to get top numEntries genes, 
 * 
 * state -> genes, setGenes - an array of genes that will be displayed; will have length of numEntries
 * useEffect(() => getAllGenes)
 * 
 * 
 * if options not set / blank graph, display "no genes displayed" in list component
 */

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
        <GeneList list={data.bio_data}/>
        <GraphView />
      </div>
 
      {(showModal && <Modal isOpen={showModal} onClose={() => setShowModal(false)}/>)}
    </div>
  );
}

export default App;
