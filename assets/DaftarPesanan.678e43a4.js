import{i as f,r as w,k as T,o as s,c as o,a as e,F as P,f as V,t as d,w as $,v as E,n as S,u as x,e as F,l as j,I as M,m as q,j as y,q as I,s as N,x as U,y as z,z as O}from"./index.42024bc3.js";const A={class:"my-6"},H={class:"flex flex-col justify-center m-auto overflow-auto"},R=e("thead",null,[e("tr",{class:"flex justify-around"},[e("th",{class:"w-[10vw]",scope:"col"},"Id"),e("th",{class:"w-[20vw]",scope:"col"},"Lokasi"),e("th",{class:"w-[10vw]",scope:"col"},"Layanan"),e("th",{class:"w-[10vw]",scope:"col"},"Harga"),e("th",{class:"w-[10vw]",scope:"col"},"Pemesan"),e("th",{class:"w-[20vw]",scope:"col"},"Petugas"),e("th",{class:"w-[10vw]",scope:"col"},"Deskripsi"),e("th",{class:"w-[15vw]",scope:"col"},"Tanggal Pemesanan"),e("th",{class:"w-[15vw]",scope:"col"},"Tanggal Penyelesaian"),e("th",{class:"w-[20vw]",scope:"col"},"Actions")])],-1),G={scope:"row",class:"w-[10vw] overflow-auto flex items-center justify-center"},J=["onClick"],K={class:"w-[20vw] overflow-auto"},Q={class:"w-[10vw] overflow-auto"},W={class:"w-[10vw] overflow-auto"},X={key:0},Y={key:1},Z={class:"w-[10vw] overflow-auto"},ee={class:"w-[20vw] overflow-auto"},te={key:0},ae=["value"],se={key:1},oe={class:"w-[15vw] overflow-auto"},le={class:"w-[15vw] overflow-auto"},ne={class:"w-[20vw]"},ce={class:"flex gap-2 justify-center items-center"},re=["onClick"],de=["onClick"],ue=["onClick"],ie={__name:"TabelDaftarPesanan",setup(B){const m=f("currentColor"),u=f("user"),_=f("data_pesanan"),l=w({}),i=w(""),p=w(""),g=w([]),b=async()=>{try{const t=await y.get("/get_karyawan");g.value=t.data}catch(t){console.log(t)}},C=t=>{l.value={},l.value[t.id]=!0,i.value=t.harga,p.value=t.karyawan.id},c=()=>{l.value={}},h=async t=>{try{await y.post("/edit_pesanan",{pesanan_id:t,harga:i.value,karyawan_id:p.value}),await D(),l.value={}}catch(r){console.log(r)}},v=async t=>{try{await y.post("/cancel_order",{order_id:t}),await D()}catch(r){console.log(r)}},k=t=>{console.log("Deskripsi")},D=async()=>{if(u.value)try{const t=await y.post("/pemesanan_list",{author_level:u.value.author_level});_.value=t.data}catch(t){console.log(t)}else router.push("/")},L=t=>{navigator.clipboard.writeText(t)};return T(()=>{b()}),(t,r)=>(s(),o("div",A,[e("table",H,[R,e("tbody",null,[(s(!0),o(P,null,V(x(_),a=>(s(),o("tr",{key:a.id,class:"border-b border-gray-700 flex justify-around w-full items-center"},[e("th",G,[e("button",{onClick:n=>L(a.id),class:"bg-sky-500 hover:bg-sky-400 text-white font-bold py-1 px-2 rounded-t"}," Copy ",8,J)]),e("td",K,d(a.lokasi),1),e("td",Q,d(a.layanan),1),e("td",W,[l.value[a.id]?(s(),o("div",X,[$(e("input",{type:"text","onUpdate:modelValue":r[0]||(r[0]=n=>i.value=n),class:"px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1",style:S({borderColor:x(m)})},null,4),[[E,i.value]])])):(s(),o("div",Y,d(a.harga),1))]),e("td",Z,d(a.pelanggan.name),1),e("td",ee,[l.value[a.id]?(s(),o("div",te,[$(e("select",{class:"px-4 py-1 bg-white dark:bg-gray-900 rounded-md border-1","onUpdate:modelValue":r[1]||(r[1]=n=>p.value=n)},[(s(!0),o(P,null,V(g.value,n=>(s(),o("option",{value:n.id},d(n.name),9,ae))),256))],512),[[F,p.value]])])):(s(),o("div",se,d(a.karyawan.map(n=>n.name).join(", ")),1))]),e("td",{class:"w-[10vw] justify-center flex items-center overflow-auto"},[e("button",{onClick:k,class:"bg-violet-500 hover:bg-violet-400 text-white font-bold py-1 px-2 rounded-t"}," Deskripsi ")]),e("td",oe,d(a.tanggal_pemesanan),1),e("td",le,d(a.tangal_selesai),1),e("td",ne,[e("div",ce,[l.value[a.id]?(s(),o("button",{key:0,onClick:n=>h(a.id),class:"bg-green-500 hover:bg-green-400 text-white font-bold py-1 px-4 rounded-t"}," Save ",8,re)):(s(),o("button",{key:1,onClick:n=>C(a),class:"bg-blue-500 hover:bg-blue-400 text-white font-bold py-1 px-4 rounded-t"}," Edit ",8,de)),e("button",{onClick:n=>v(a.id),class:"bg-red-500 hover:bg-red-400 text-white font-bold py-1 px-4 rounded-t"}," Delete ",8,ue),l.value[a.id]?(s(),o("button",{key:2,onClick:c,class:"text-3xl rounded-full h-min w-min relative right-2"},[j(x(M),{icon:"ic:twotone-cancel"})])):q("",!0)])])]))),128))])])]))}},ve={class:"flex flex-col justify-center my-12 text-center md:text-sm text-xs"},we=e("h1",null,"Daftar Pesanan",-1),pe={__name:"DaftarPesanan",setup(B){const m=I(),u=w([]),_=w([]),l=w(""),i=f("user"),p=f("currentColor");N("data_pesanan",_);const g=(c,h)=>c.filter(v=>Object.keys(v).some(k=>typeof v[k]=="string"&&v[k].toLowerCase().includes(h.toLowerCase()))),b=()=>{const c=g(u.value,l.value);_.value=c},C=async()=>{if(i.value)try{const c=await y.post("/pemesanan_list",{author_level:i.value.author_level});u.value=c.data}catch(c){console.log(c)}else m.push("/")};return U(async()=>{await C(),_.value=u.value}),z(u,()=>{b()},{deep:!0}),(c,h)=>(s(),o("div",ve,[we,j(O,{searchClass:"w-[24rem] h-10 pl-8 pr-2 rounded-lg",modelValue:l.value,"onUpdate:modelValue":h[0]||(h[0]=v=>l.value=v),inputClass:"text-sm md:text-base",submitFunc:b,class:"m-auto my-4",style:S({borderColor:x(p)})},null,8,["modelValue","style"]),j(ie)]))}};export{pe as default};
