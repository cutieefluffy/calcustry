import streamlit as st


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Menu",("Home","Tentang Massa Atom Relatif", "Aplikasi", "Perhitungan Massa Atom Relatif","Perhitungan Normalitas"))
if add_selectbox=="Home":
    
    st.subheader("Hi! Kami siap membantumu! 👋🏻")
    st.subheader("created by :")
    st.subheader("KELOMPOK 11 (1D - ANKIM)")
    st.write (''' the member of the team :
          
1. R.A. Nailha Ilham (2360226)
2. Fadhil Januar (2360118)
3. Patimah Azzahra (2360223)
4. Yuliansyah Faizin Akbar (2360293)
5. Zahrani Faradisa (2360298)
''')
    
    
    
elif add_selectbox == "Tentang Massa Atom Relatif" :
    st.title(" Massa Atom Relatif")
    st.subheader ("Apa itu massa tom relatif?")
    st.write("Massa atom relatif adalah massa suatu atom yang ditentukan dengan cara membandingkan dengan massa atom standar. Massa atom relatif, disingkat dengan Ar. Berdasarkan IUPAC (International Union of Pure and Applied Chemistry) yang digunakan sebagai standar penentuan massa atom relatif adalah atom karbon.")
    st.subheader("Rumus Massa Atom Relatif")
    st.write("Ar Unsur X= massa rata-rata unsur X : 1/12 x massa atom C-12")
    
elif add_selectbox =="Aplikasi" :
    st.title("Aplikasi Mengetahui Atom Relatif Unsur")
    unsur = st.text_input('Masukkan lambang/symbol unsur kimia ex;Fe')
    tombol = st.button('Tampilkan nilai Massa Atom Relatif')


#Percabangan lebih dari dua kasus
    if unsur == "H" :
        st.success ("1")
    elif unsur == "Li" :
        st.success ("7")
    elif unsur == "Na" :
        st.success ("23")
    elif unsur == "K" :
        st.success ("39")
    elif unsur == "Rb" :
        st.success ("85,5")
    elif unsur == "Cs" :
        st.success ("133")
    elif unsur == "Fr" :
        st.success ("223")
    elif unsur == "Be" :
        st.success ("9")
    elif unsur == "Mg" :
        st.success ("24,3")
    elif unsur == "Ca" :
        st.success ("40")
    elif unsur == "Sr" :
        st.success ("88")
    elif unsur == "Ba" :
        st.success ("137")
    elif unsur == "Ra" :
        st.success ("226")
    elif unsur == "Ra" :
        st.success ("226")
    elif unsur == "Sc" :
        st.success ("45")
    elif unsur == "Y" :
        st.success ("89")
    elif unsur == "Ti" :
        st.success ("48")
    elif unsur == "Zr" :
        st.success ("91,2")
    elif unsur == "Hf" :
        st.success ("178,5")
    elif unsur == "Rf" :
        st.success ("267,1")
    elif unsur == "B" :
        st.success ("11")
    elif unsur == "Al" :
        st.success ("27")
    elif unsur == "Ga" :
        st.success ("70")
    elif unsur == "In" :
        st.success ("115")
    elif unsur == "Tl" :
        st.success ("204,4")
    elif unsur == "Uut" :
        st.success ("289")
    elif unsur == "C" :
        st.success ("12")
    elif unsur == "Si" :
        st.success ("28,1")
    elif unsur == "Ge" :
        st.success ("73")
    elif unsur == "Sn" :
        st.success ("119")
    elif unsur == "Pb" :
        st.success ("207,2")
    elif unsur == "Fl" :
        st.success ("289,2")
    elif unsur == "Nh" :
        st.success ("286,2")
    elif unsur == "Lu" :
        st.success ("175")
    elif unsur == "Lr" :
        st.success ("262,1")
    elif unsur == "V" :
        st.success ("51")
    elif unsur == "Nb" :
        st.success ("93")
    elif unsur == "Ta" :
        st.success ("181")
    elif unsur == "Db" :
        st.success ("262")
    elif unsur == "Cr" :
        st.success ("52")
    elif unsur == "Mo" :
        st.success ("96")
    elif unsur == "W" :
        st.success ("184")
    elif unsur == "Sg" :
        st.success ("266")
    elif unsur == "N" :
        st.success ("14")
    elif unsur == "P" :
        st.success ("31")
    elif unsur == "As" :
        st.success ("75")
    elif unsur == "Sb" :
        st.success ("122")
    elif unsur == "Bi" :
        st.success ("209")
    elif unsur == "Uup" :
        st.success ("288")
    elif unsur == "Mc" :
        st.success ("289,2")
    elif unsur == "O" :
        st.success ("16")
    elif unsur == "S" :
        st.success ("32")
    elif unsur == "Se" :
        st.success ("79")
    elif unsur == "Te" :
        st.success ("128")
    elif unsur == "Po" :
        st.success ("209")
    elif unsur == "Lv" :
        st.success ("293.2")
    elif unsur == "Mn" :
        st.success ("55")
    elif unsur == "Tc" :
        st.success ("99")
    elif unsur == "Re" :
        st.success ("186,2")
    elif unsur == "Bh" :
        st.success ("264")
    elif unsur == "Fe" :
        st.success ("56")
    elif unsur == "Ru" :
        st.success ("101")
    elif unsur == "Os" :
        st.success ("190,2")
    elif unsur == "Hs" :
        st.success ("269")
    elif unsur == "Co" :
        st.success ("59")
    elif unsur == "Rh" :
        st.success ("103")
    elif unsur == "Ir" :
        st.success ("192,2")
    elif unsur == "Mt" :
        st.success ("268")
    elif unsur == "Ni" :
        st.success ("59")
    elif unsur == "Pd" :
        st.success ("106,4")
    elif unsur == "Pt" :
        st.success ("195")
    elif unsur == "Ds" :
        st.success ("269")
    elif unsur == "F" :
        st.success ("19")
    elif unsur == "Cl" :
        st.success ("35,5")
    elif unsur == "Br" :
        st.success ("80")
    elif unsur == "I" :
        st.success ("127")
    elif unsur == "At" :
        st.success ("210")
    elif unsur == "Uus" :
        st.success ("292")
    elif unsur == "He" :
        st.success ("4")
    elif unsur == "Ne" :
        st.success ("20,2")
    elif unsur == "Ar" :
        st.success ("40")
    elif unsur == "Kr" :
        st.success ("85")
    elif unsur == "Xe" :
        st.success ("131,3")
    elif unsur == "Rn" :
        st.success ("222")
    elif unsur == "Uuo" :
        st.success ("293")
    elif unsur == "La" :
        st.success ("139")
    elif unsur == "Ce" :
        st.success ("140")
    elif unsur == "Pr" :
        st.success ("141")
    elif unsur == "Nd" :
        st.success ("144")
    elif unsur == "Pm" :
        st.success ("145")
    elif unsur == "Sm" :
        st.success ("150")
    elif unsur == "Eu" :
        st.success ("152")
    elif unsur == "Gd" :
        st.success ("157")
    elif unsur == "Td" :
        st.success ("159")
    elif unsur == "Dy" :
        st.success ("162")
    elif unsur == "Ho" :
        st.success ("165")
    elif unsur == "Er" :
        st.success ("167")
    elif unsur == "Tm" :
        st.success ("169")
    elif unsur == "Yb" :
        st.success ("173")
    elif unsur == "Lu" :
        st.success ("175")
    elif unsur == "Ac" :
        st.success ("227")
    elif unsur == "Th" :
        st.success ("232")
    elif unsur == "Pa" :
        st.success ("231")
    elif unsur == "U" :
        st.success ("238")
    elif unsur == "Np" :
        st.success ("237")
    elif unsur == "Pu" :
        st.success ("244")
    elif unsur == "Am" :
        st.success ("243")
    elif unsur == "Cm" :
        st.success ("247")
    elif unsur == "Bk" :
        st.success ("247")
    elif unsur == "Cf" :
        st.success ("251")
    elif unsur == "Es" :
        st.success ("254")
    elif unsur == "Fm" :
        st.success ("257")
    elif unsur == "Md" :
        st.success ("258")
    elif unsur == "No" :
        st.success ("259")
    elif unsur == "Lr" :
        st.success ("262")
    else :
        st.success (" ")


        
elif add_selectbox=="Perhitungan Massa Atom Relatif" :
    st.title('Perhitungan Massa Atom Relatif')
    
    massa_rata_rata_1_atom_x= st.number_input('Masukkan Massa Rata-Rata 1 Atom (x 10^-23)')
    massa_atom_C_12= st.number_input('Masukkan Massa Atom C-12 (x 10^-23)')
    tombol = st.button('Hitung Massa Atom Relatif')
    if tombol :
        Massa_Ar = massa_rata_rata_1_atom_x*10*(-23)/(1/12*massa_atom_C_12*10*(-23))
        st.success(f'Massa Atom Relatif adalah {Massa_Ar}')
        
elif add_selectbox=="Perhitungan Normalitas":
    st.title('Perhitungan Normalitas')
    massa= st.number_input('Masukkan Massa (mgram)')
    BE= st.number_input('Masukkan BE/BM')
    Volume=st.number_input ('Masukkan Volume (mL)')
    FP=st.number_input ('Masukkan FP (jika tidak ada FP masukkan angka 1 sebagai FP )')
    tombol = st.button('Hitung Normalitas')
    if tombol :
        Normalitas = massa/(FP*Volume*BE)
        st.success(f'Normalitas adalah {Normalitas}')