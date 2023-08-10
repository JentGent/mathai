import os

# i pasted the result of this into INDEX_TO_TOKEN
def vocab_from_data(path_to_training_data):
    vocab = sorted(list("rnT=Iw+Z*Q3o&:t(0Ampi_U1'5)}{;\\XhvRa[u/GLM\n~WDKJH>k# jO<B!-cex9Sf8]s.y,d|PFNq64zl$b72E`g\"YVC^"))
    with open(path_to_training_data, "r") as file:
        while line := file.readline():
            line = line.strip()
            if line.startswith("$"):
                vocab = list(set(vocab + line.split()))
            else:
                vocab = list(set(vocab + " ".join(line.split()[1:]).split()))
    vocab = sorted(set(vocab + ["  "]), key=len, reverse=True)
    return vocab

# print(vocab_from_data(os.path.join(os.path.dirname(__file__), "data.txt")))

NAME_START_TOKEN = "<NAME START>"
NAME_END_TOKEN = "<NAME END>"
SECTION_DELIMITER_TOKEN = "<SECTION DELIMITER>"
INDEX_TO_TOKEN = [NAME_START_TOKEN, NAME_END_TOKEN, SECTION_DELIMITER_TOKEN, 'pMatToMatPoly', 'cPolyMatToMat', 'ConstPolyMat', 'inftyexpitau', 'ComplUSGraph', 'cyclShiftOLD', 'GoldbachEven', 'TarskiGDim>=', 'matToPolyMat', 'GoldbachOddW', 'InnerFiveSeg', 'OuterFiveSeg', 'polySplitLim', 'TransportTo', 'FriendGraph', '-1-1-onto->', 'GoldbachOdd', 'ClWWalksNOn', 'Irreflexive', 'RingCatALTV', 'hereditary', 'WSPathsNOn', 'EulerPaths', 'decompPMat', 'RegUSGraph', 'FinUSGraph', 'CPreHilOLD', 'selectVars', 'RngCatALTV', 'Singletons', 'Pell1234QR', 'sigAlgebra', 'CharPlyMat', 'DivRingOps', 'ComplGraph', 'subringAlg', 'toCaraSiga', 'CnvRefRels', 'ldgIdlSeq', 'ClWWalksN', 'CovHasRef', 'tarskiMap', 'cyclShift', 'CnvRefRel', 'ExtStrCat', 'NeighbVtx', 'WWalksNOn', 'inftyexpi', 'normOpOLD', 'TarskiG2D', 'mzPolyCld', 'OutsideOf', 'toCPreHil', 'spliceOLD', 'splitFld1', 'minPolyAA', '-TopMgm->', 'ConnGraph', 'TarskiGCB', 'N-Locally', 'Reflexive', 'Singleton', 'ScMatALT', 'CRingOps', 'splitFld', 'IntgOver', 'Colinear', 'maVecMul', 'USHGraph', 'SPathsOn', 'toNrmGrp', 'BndLinOp', 'uncurry_', 'ElEqvRel', 'SubGraph', 'ringLMod', 'Pell14QR', 'TarskiGE', 'RingSpan', 'RegGraph', 'Paracomp', 'EdgWalks', 'Circuits', 'idlGen1p', 'freeLMod', 'TarskiGB', 'PosetRel', 'ordPwSer', 'TrailsOn', 'Restrict', 'GrpOpHom', 'IntgRing', 'CCinftyN', 'USPGraph', 'toUnifSp', 'PellFund', 'WSPathsN', 'evalSub1', 'CSGrpALT', 'TarskiGC', 'DiagFunc', 'assIntOp', 'measures', 'minMatR1', 'CHStates', 'TopBases', 'ClWWalks', 'mFromItp', 'cplMetSp', 'BernPoly', 'TosetRel', 'TopDRing', 'FermatNo', 'SubDRing', 'uncurryF', 'LPlanes', 'NrmCVec', 'UnifSet', 'clIntOp', 'polyFld', 'sigaGen', 'varFMnd', 'ClSubSp', 'AlgSpan', 'UPGraph', 'freeGrp', 'TopOpen', 'FuncCat', 'LSAtoms', 'linIndS', 'DivRing', 'CVecOLD', 'matRepV', 'mVSubst', 'DMatALT', 'PrPairs', 'toMetSp', 'freeMnd', 'evalSub', 'CCinfty', 'BaseSet', 'Locally', 'TarskiG', 'reverse', 'EqvRels', 'Funpart', 'CnvRefs', 'SubRing', 'setrecs', 'mRSubst', 'repeatS', 'SemiGrp', 'CauFilU', 'CaraGen', 'finSupp', 'SymRels', 'RngHomo', 'TopRing', 'RefRels', 'UnivVtx', 'unifTop', 'FullFun', 'pstoMet', 'HomLimB', 'NrmSGrp', 'linDepS', 'RingOps', 'class-o', 'PathsOn', 'UMGraph', '-onto->', 'LFinGen', 'RngIsom', 'UHGraph', 'FiveSeg', 'ClWalks', 'RiseFac', 'SGrpALT', 'UPWalks', 'USGraph', 'OutMeas', 'Monic1p', 'Pell1QR', 'CHilOLD', 'NrmRing', 'EDRingR', 'unitVec', 'rRndVar', 'CUnifSp', 'RingCat', 'uncurry', 'varFGrp', 'RingHom', 'subMat1', 'LinesEE', 'RingIso', 'CMgmALT', 'FallFac', 'CPreHil', 'WWalksN', 'MetOpen', 'toOMeas', 'toPoly1', 'metUnif', 'WalksOn', 'class-n', 'matRRep', 'LPIdeal', 'VtxDeg', 'subMat', 'elwise', 'CycGrp', 'SetCat', 'UnifOn', 'curryF', 'fClusf', 'IdlGen', 'substr', 'ManTop', 'Points', 'GrpAct', 'PreHil', 'IndMet', 'litMat', '-1-1->', 'quot1p', 'GrpIso', 'arcsin', 'LCDual', 'arccos', 'NrmMod', 'DirRel', 'Ddelta', 'RngHom', 'eqltrG', 'Limits', 'Cauchy', 'Domain', 'mFresh', 'TopSet', 'topGen', 'oppCat', 'Bigcup', 'normop', 'filGen', 'HAtoms', '_/_\\^n', 'LIdeal', 'EDRing', 'WWalks', 'normOp', 'GrpHom', 'MblFnM', 'ZZring', 'normCV', 'pmEven', 'AssAlg', 'AlgInd', 'RefRel', 'HomLim', '*MetSp', 'GrIsom', 'Subcat', 'mPSDer', 'Moore_', 'mSubst', 'CHOICE', 'SubMnd', 'SubGrp', 'MgmALT', 'TopVec', 'TopGrp', 'CauFil', 'RePart', 'CovMap', 'States', '-Mgm->', 'SymGrp', 'RPrime', 'normfn', 'eigval', 'InaccW', 'CondEq', 'ketbra', 'FilMap', 'UnifSp', 'mulGrp', '2Ideal', 'eigvec', 'CMetSp', 'SalGen', 'Struct', 'oField', '-Top->', 'comLaw', 'IsomGr', 'Tarski', 'TotBnd', 'RR*Hom', 'wUniCl', 'ContFn', 'seqstr', 'NoeACS', 'curry_', 'Dirset', 'prefix', 'assLaw', 'CatCat', 'minfty', 'LocFin', 'PrjSpn', 'PrRing', 'NrmVec', 'SMblFn', 'WAtoms', 'UnifSt', 'maAdju', 'TopMnd', 'TopMod', 'TrRels', 'AbsVal', 'PolyAP', '<_O(1)', 'HDMap1', 'PSubCl', 'LSubSp', 'RngCat', 'ordTop', 'TopSep', 'RngIso', 'PSubSp', 'setvar', 'ContOp', 'mPwSer', 'FinSum', 'Ramsey', 'OrdIso', '-Set->', 'Proset', 'liminf', 'NrmGrp', 'SPaths', 'MonoAP', 'gcdOLD', 'Lambda', 'Cycles', 'Scalar', 'Unic1p', 'idFunc', 'pmTrsp', 'NzRing', 'TrPred', 'TopLnd', 'SymRel', 'BrSiga', 'AbelOp', 'splice', 'mPreSt', 'arctan', 'limsup', 'PwSer1', 'wl-el2', 'MgmHom', 'o.func', 'mStRed', 'MndHom', 'Sphere', 'OBasis', 'mzPoly', 'pinfty', 'EqvRel', 'MaxIdl', 'LLines', 'Trails', 'LBasis', 'SubMgm', 'proj1', 'Faith', 'oRing', 'mrInd', 'RRHom', 'RRExt', 'mPoly', 'EEhil', 'SalOn', 'LVols', 'Range', 'HDMap', 'Seg<_', 'Homeo', 'DIsoC', 'dProj', 'PtFin', 'HGMap', 'MblFn', 'AtLat', 'Toset', 't*rec', 'pprod', 'PrIdl', 'LinOp', 'Poly<', 'Prime', 'Moore', 'GF_oo', 'frecs', 'NMHom', 'gamma', 'infty', 'RRfld', 'Magma', 'MetSp', 'mStat', 'LNoeR', 'Pairs', 'LDual', 'tsums', 'LineG', 'log_G', 'MndOp', 'LSHyp', '.iOLD', 'maDet', 'Arrow', 'TopSp', 'perpG', 'Apply', 'AxReg', 'PConn', 'CRing', 'RSpan', 'Field', 'SRing', 'DIsoH', 'mESyn', 'mGMdl', "iota'", 'prod_', 'LMHom', 'NGHom', '*Ring', 'ZRing', 'class', 'SConn', 'coeff', 'aleph', 'AxRep', 'PrjSp', '_TrFo', 'DProd', 'Trans', 'Poset', 'TEndo', 'lInvG', 'RR>=0', 'LIndS', 'fClus', 'Undef', 'fLimf', 'RLReg', 'Image', 'denom', 'AxExt', 'CChat', 'digit', 'projh', 'cprob', 'evalF', 'LNoeM', 'CCbar', 'clLaw', '.sOLD', 'LineM', 'SubSp', 'limCC', 'intOp', 'lastS', 'degAA', 'MEndo', 'ZRHom', 'Archi', 'CCfld', 'Fin1a', 'GrpOp', 'line3', 'HrmOp', 'DVecA', 'numer', 'seqom', 'HVMap', 'LMIso', '|`cat', 'pInvG', 'defAt', 'mTree', 'mPPSt', 'Dioph', 'wl-el', 'LSSum', 'wl-in', 'Disj_', 'mEval', 'mFRel', 'ZeroO', 'LinFn', 'shift', 'toInc', 'limPt', 'IDomn', 'mWGFS', 'compA', 'SLMod', 'Paths', 'mVars', 'AxPow', 'mHomP', 'joinH', 'LinCo', '-cn->', 'Inacc', 'sigma', 'mUSyn', 'iota_', 'BLnOp', 'TopOn', 'InitO', 'C_cat', 'Walks', '_pred', 'RRhat', 'UniOp', 'PsMet', 'maMul', 'LIndF', 'DVecH', 'PHtpy', 'Ismty', 'voln*', 'rem1p', 'Irred', '_FrSe', 'mType', 'curry', 'TrRel', 'ScMat', 'algSc', 'pairF', 'Lines', 'LSpan', 'wrecs', '_trCl', 'DIsoA', 'Monic', 'HLHil', 'Poly1', 'Fibci', 'iomnn', 'normh', 'Atoms', 'pmSgn', 'AxInf', 'theta', 'RRbar', 'RRVec', 'mrCls', 'QQHom', 'eval1', 'DIsoB', 'CnExt', 'ODual', 'QpOLD', 'TermO', 'CvLat', 'oRVC', '.(x)', 'area', 'Slot', 'oppG', 'kGen', '|^|_', 'PtDf', 'norm', 'Fin2', 'Ldlf', '2ndF', 'HmOp', '0vec', 'invg', 'sum*', 'Retr', 'RR>0', 'Comp', 'pCnt', 'Haus', 'pmap', '~=ph', 'iEdg', 'Even', 'Cntr', 'sSet', 'ZZ>=', 'dist', 'mapd', '[]NN', 'mREx', 'itgm', '2ndc', 'Proj', '_/_\\', 'mSAX', 'Fmla', '_Old', 'qTop', 'LnOp', 'Clsd', 'WLim', 'cosh', 'LPol', 'join', 'Base', 'sinh', 'fBas', 'mItp', 'Z/nZ', 'oppR', 'Diag', 'bday', '<->g', 'Full', 'DLat', '.(+)', 'tail', 'cgrA', 'toTG', '~~>v', 'coe1', 'iota', 'CVec', '(+)m', 'Succ', 'mSyn', "''''", 'Fin3', 'pGrp', 'Com2', 'sitg', 'midG', 'CMod', 'Abel', 'Syms', 'oGrp', 'PNrm', '1stF', 'LHyp', 'sum_', '_lcm', 'm0St', 'LTrn', 'SSet', 'Univ', 'domA', 'comf', 'sqrt', 'LPIR', 'ch0_', 'Fin7', 'oMnd', 'PAut', '~~>u', 'Line', 'Domn', 'Plig', 'Prob', 'voln', 'rank', 'mCls', 'Sect', 'bits', 'LVec', 'Tayl', 'Z[i]', 'NN0*', 'Perf', '_|_P', 'Conn', 'var1', 'Refs', 'vol*', 'cadd', 'CytP', 'CLat', 'comp', 'linC', 'span', 'tpos', 'LDil', 'CMnd', 'sitm', 'Cart', 'invc', 'Unit', '1/_G', 'zeta', 'mGFS', 'log_', 'sadd', 'toHL', 'card', '_Ind', 'mVar', 'Mono', 'Rels', 'tanh', 'Func', 'SAlg', 'LFnl', 'LMod', 'TGrp', 'mDeg', 'adjh', 'Htpy', 'recs', '<bag', 'gsum', 'pSyl', 'hadd', 'ball', 'null', 'wsuc', 'Funs', 'Isom', 'O(1)', 'LAut', '1stc', 'HomA', 'cgrG', 'Fin5', '*Met', '0hop', 'proj', 'sgns', 'mThm', 'logb', 'CBan', 'Cgr3', '~~>r', 'smul', 'sngl', 'HomF', 'ExId', 'Cntz', 'mUFS', 'RR*s', 'deg1', 'Fin4', 'CMet', 'WUni', 'UFil', 'Kol2', 'Fin6', 'codA', '._|_', 'SatE', '~~>t', '[C.]', '~~>*', 'Reds', 'Ring', 'invr', 'SGrp', 'fLim', 'Homf', 'LKer', 'ZMod', '~<_*', 'meet', 'Btwn', 'DChr', 'Word', 'sum^', 'quot', '_tau', 'AxUn', 'Pred', 'supp', 'repr', 'Poly', 'HCmp', 'Meas', 'mMdl', '->..', 'CHil', 'DMat', '<_op', 'CNrm', 'eval', '~Met', 'Ismt', 'Img', 'o1_', "rh'", 'B1_', 'RR3', '.+b', 'v"_', 'Fne', 'sgn', 'jch', '.0.', 'mAx', 'Fix', '_pi', 'NN0', 'O1_', 'ta1', '-op', 'Xc.', 'Smo', '+op', 'Yon', 'b1_', 'if-', 'log', 'rh0', 'ph"', 'Cgr', 'mVL', 'pr1', 'F/_', '.||', 'cos', '_ZZ', 'G1_', 'Iop', 'uCn', '->g', 'c1_', 'Inv', './\\', 'GId', 'IdA', 'C^n', '.op', 'Cup', 'chr', 'Iso', 'Fre', '.x.', 'RR+', 'sup', 'Met', 'inf', '_om', 'ta"', '[,]', 'hlG', 'Dil', '-oo', '.X.', 'leA', '|->', 'PID', 'Ban', '/\\g', 'piN', 'rec', '.pQ', 'UFL', 'csc', 'th1', 'vts', 'psi', 'XX.', 'Fld', 'mCN', 'a0_', '|`f', '.ih', 'lcm', 'ocv', 'e//', 'si0', 'F1_', '<RR', 'jsi', 'Mnd', '.if', "th'", '.xb', 'Prv', '+oo', 'Odd', '~FG', 'jth', '.<_', '\\/H', 'mST', 'Cau', 'jet', '.P.', '^pm', '1st', 'et"', '-cc', 'Fin', "ph'", 's"_', '2nd', 'gcd', 'OmN', 'o0_', 'bra', 'har', 'jze', 'Lim', 'ps1', '...', 'S.2', 'Nat', '+fn', '||r', 'Ass', '->.', 'rh1', 'inl', 'Dmn', '*rf', 'ocH', 'Vtx', 'red', '[,)', 'ch"', 'Ana', '~=g', 'ppi', 'Cap', 'Sat', '-->', 'adj', 'Reg', '..^', 'mUV', 'ACS', 'mod', 'o"_', 'wff', '~=R', '|^|', 'sin', 'a1_', 'Bnd', 'e.g', 'GCH', "ps'", 'si1', '|_|', "v'_", 'S.1', 'E.g', 'Itv', 'ze"', 'PCl', 'et1', '.sf', 'th"', '-1R', 'mVR', 'R1_', 'gEx', 'C1_', 'AFS', 'Ref', 'Cat', 'trL', 'dim', 'H1_', '<_s', 'abs', 'Prt', "'''", 'Rel', 'int', '_Qp', 'A.g', '(,]', 'f0_', 'mDV', 'Lam', 'si"', 'CNF', 'Ray', 'seq', '<pQ', '~=c', 'ps"', 'odZ', '+cc', '0op', 'L^1', '+P.', 'jrh', 'jph', 'mmu', 'jmu', 'Xs.', 'rmX', 'Xs_', '-/\\', '<oL', '.ef', 'D1_', 'mSA', 'ps0', '.1.', 'cls', 'ze0', '<->', "si'", 'hpG', 'Hom', '~=m', 'mVT', 'Fil', 'Hil', 'mTC', 'Mgm', '.cc', 'c0_', '.\\/', '+pQ', 'Grp', '_|_', 'ph1', 'Lat', 'Idl', 'glb', '.0b', 'EEG', "ze'", 'lub', 'Arg', 'RR^', 'Epi', '~~>', '_Cc', 'rh"', 'raG', 'ndx', "et'", '/Qp', 'L1_', 'A1_', 'Trn', 'Xt_', '(x)', "ch'", '~ae', '.+^', 'MH*', '\\/_', '<oH', "s'_", '~QG', 'tag', 'ran', '.o.', 'I1_', 'suc', 'mFS', '|`s', 'ch1', 'Fun', 'mEx', 'V1_', 'inA', '1/2', 'et0', 'Red', 'oFC', 'Rng', '(/)', '<rr', '|X.', 'exp', 'pi1', 'S1_', 'pr2', 'ph0', '<<<', 'phi', 'M1_', 'leG', 'jla', '=/=', '-.g', '/_\\', 'Om1', 'inv', 'sec', 'Nrm', 'ta0', 'CnP', 'Trs', 'dom', 'Edg', 'mVH', 'cot', 'Top', 'jps', '|`t', '_Se', 'ocA', 'E**', 'Mat', '<<s', 'th0', '.fn', '(,)', 'jta', '\\/g', '~=r', 'Ord', 'tan', 'C_H', 'i^i', '~Qp', 'n0_', 'OML', 'nei', '~<_', '^ko', 'AC_', '/_f', "ta'", 'rmY', 'b0_', 'RR*', '|`v', "o'_", 'vol', 'deg', 'ze1', 'inr', 'E1', '1.', '<"', 'A!', "C'", '|g', "E'", "G'", 'x.', '4o', 'U_', 'e0', 'R0', 'V"', "L'", 'u1', 'y"', '.+', 'Rn', 'o.', 'p"', 'L0', "X'", 'd"', '*Q', 'e/', 'n"', "f'", 'G"', '+c', 'P.', 't*', 'cf', 'QQ', '+-', 'U"', "J'", 'Or', '||', '.g', 'OL', "c'", '^r', '|^', '>.', 'X1', '<.', '0g', 'z1', 'J0', '[s', 'K0', '>_', '++', 'HL', '<Q', 't0', 'T1', 'q"', 'E!', '_G', 'H"', '~=', 'ch', 's1', 'd0', '+Q', 'X"', 'Cp', '-R', '1R', '{R', "t'", '<_', 'T0', 'Y1', 'Xp', 'h0', "z'", 'i"', '_O', "u'", 'Se', "h'", 'r*', "M'", '-h', 'Po', '$=', 'Z"', 'I0', '"s', ']s', 'Tr', 'k"', '^m', 'N0', 'V0', '3o', 'z0', '^s', 'On', '0p', '^c', 'P"', '|_', "e'", 'c"', '(.', '/e', '_i', '/Q', "P'", '#p', 'l"', 'Zp', '_N', 'u0', '.*', './', "T'", '].', 'S_', '~H', '\\/', 'Cn', '$p', '<o', '+f', '|s', '.<', "O'", '|)', 'E"', '.r', "l'", 'A"', '${', 'S"', 'F.', "B'", '~<', '->', '0R', 'tX', 'w0', 'oF', '=g', 'p1', 'E*', "b'", '_e', '_R', 'oR', 'Id', '+R', '2o', 'N"', '(|', 'ka', '.^', 'oc', 'NN', '.~', 'S.', "V'", "Z'", "r'", '==', 't1', "Q'", 'M"', '+H', '((', 'f"', '/r', '+v', 'v0', 'j1', 'b"', 'D"', '.-', 'U1', 'T"', 'C"', '.Q', '.o', 'th', 'Q"', 'MH', 'r0', 'i0', '1P', '-v', 'C_', "K'", 'fi', "i'", 'm0', 'le', '_M', 'ze', ').', 'r"', 'We', 'A.', '.s', '^o', '1o', '.R', 'ZF', 'rh', 'w"', 'O0', 'Hf', 'KQ', '+e', 'E.', 'si', "`'", 'GF', '$a', '/s', 'j0', 'Q0', ',.', 'SH', 'z"', '~~', 'ZZ', 'k0', '$d', '_C', 'G0', 'h"', '.N', '-g', '_E', 'H0', 'a"', 'x"', "g'", 'F"', 'D0', 'M0', '0h', '/L', "a'", 'f1', '.i', 'CH', '">', '|=', "N'", 's0', '-u', '.,', "R'", 'k1', '>>', 'U.', "w'", '[_', 'W0', '_L', 'T.', 'ta', 'd1', '<<', ',~', 'Re', '_V', 'l1', 'I"', '+P', 'h1', 'Fr', 'x1', 'UB', ']_', "n'", 'Er', 'lt', '*p', 'B"', "H'", 'Im', "k'", '+r', 'X_', 'if', 'AP', "I'", '$c', '/g', '+N', '+o', 'II', 't"', 'g"', '1r', 'LB', 'y1', 'sX', 'N.', '|-', '0.', '-r', 'x0', '$v', 'R"', 'od', 'Y"', 't+', '$.', '~R', '$f', '$}', '  ', 'TC', ',,', '_D', "x'", 'B0', '#b', "j'", 'X.', 'u.', 'C.', '[b', 'Z1', 'p0', "A'", 'm1', '))', 'g1', 'CC', '<P', '*e', 'v1', 'Q1', 'S0', 'A0', 'F/', 'q1', 'No', 'O"', 'Q.', '~P', "W'", '+g', "Y'", "p'", 'AA', 'g0', 'e1', 'ae', 'vA', 'w1', 'J1', 'P0', '<N', 'm"', '+h', 'RR', 'F0', '~Q', ']b', 'e"', '_S', 'cm', 'Dn', 'Y0', "U'", 'U0', '/.', 'EE', "D'", '1Q', 'Qp', 'Z0', '.h', '-e', 'K1', '0H', 'C0', 'R.', 'W"', 'l0', '/b', 'u"', '[.', '=>', '|`', 'K"', 'L"', '.v', 'OP', 'ps', 'ph', '<s', 'P1', 'N1', 'y0', '/\\', 'la', '^^', 'R1', "y'", 'vH', 'n1', 'j"', '<R', '-.', 'et', 'E0', 'mu', 'J"', 'Pg', '$e', "q'", 'e.', 'W1', '_d', '*r', "m'", "F'", 'X0', '_I', 'i1', 'Fn', 'r1', 'q0', "d'", "S'", 'S', 'v', ']', 'E', 'i', 'k', 'a', 'h', '7', ')', '[', ':', 'I', 'V', '\n', '5', 'u', '=', '|', 'T', 'z', '3', 't', '^', 'D', 'r', 'l', '2', '*', '\\', '`', '1', 's', '"', 'M', 'p', 'x', 'e', 'L', 'j', '0', 'J', 'Z', '4', '$', 'n', 'Q', 'o', '!', 'R', ';', '6', 'A', ',', '+', 'G', '9', '8', '~', "'", 'm', 'q', 'H', ' ', 'P', '_', 'X', 'K', 'Y', '}', 'f', '&', 'F', 'g', '.', 'B', 'C', 'U', 'W', 'w', '{', 'y', 'O', '/', 'b', 'd', 'c', '<', '(', '#', '>', 'N', '-']
VOCAB_SIZE = len(INDEX_TO_TOKEN) # 1674
TOKEN_TO_INDEX = { token: index for index, token in enumerate(INDEX_TO_TOKEN) }
NAME_START_INDEX = TOKEN_TO_INDEX[NAME_START_TOKEN]
NAME_END_INDEX = TOKEN_TO_INDEX[NAME_END_TOKEN]
SECTION_DELIMITER_INDEX = TOKEN_TO_INDEX[SECTION_DELIMITER_TOKEN]

_scope = 0
_num_proofs = 0
_longest_section = 0
_current_proof = 0
_section_indices = []
def add_token(token_ids, line, i, line_length):
    global _scope
    global _num_proofs
    global _longest_section
    global _current_proof
    global _section_indices
    if i >= line_length or (line[i] == " " and (i + 1 >= line_length or line[i + 1] != " ")):
        return 1
    remaining_text = line[i:]
    for token in INDEX_TO_TOKEN:
        if remaining_text.startswith(token):
            if token == "${":
                if _scope == 0:
                    _section_indices.append(len(token_ids))
                    token_ids.append(SECTION_DELIMITER_INDEX)
                    _num_proofs += 1
                    print("proof #", _num_proofs)
                    print("longest section:", _longest_section)
                if _current_proof > _longest_section:
                    _longest_section = _current_proof
                _current_proof = 0
                _scope += 1
            elif token == "$}": _scope -= 1
            token_ids.append(TOKEN_TO_INDEX[token])
            _current_proof += 1
            return len(token)
    return 1
def encode(text):
    global _current_proof
    token_ids = []
    lines = text.split("\n")
    for line in lines:
        line_length = len(line)
        i = 0
        stripped = line.strip()
        if stripped.startswith("$"):
            while i < line_length: i += add_token(token_ids, line, i, line_length)
        else:
            reached_name = False
            while i < line_length:
                if not reached_name and line[i] != " ":
                    reached_name = True
                    token_ids.append(TOKEN_TO_INDEX[NAME_START_TOKEN])
                    _current_proof += 1
                    while i < line_length and line[i] != " ":
                        token_ids.append(TOKEN_TO_INDEX[line[i]])
                        _current_proof += 1
                        i += 1
                    token_ids.append(TOKEN_TO_INDEX[NAME_END_TOKEN])
                    _current_proof += 1
                i += add_token(token_ids, line, i, line_length)
        token_ids.append(TOKEN_TO_INDEX["\n"])
    return token_ids

def decode(token_ids):
    text = ""
    naming = False
    for i, token_id in enumerate(token_ids):
        token = INDEX_TO_TOKEN[token_id]
        if token == NAME_START_TOKEN:
            naming = True
            continue
        if token == NAME_END_TOKEN:
            naming = False
            text += " "
            continue
        if token == SECTION_DELIMITER_TOKEN: continue
        text += token
        if token != "\n" and not token.isspace() and not naming and i < len(token_ids) and (i + 1 >= len(token_ids) or INDEX_TO_TOKEN[token_ids[i + 1]] != "\n"):
            text += " "
    return text

def generate_bin(path_to_training_data, path_to_bin, path_to_sections):
    with open(path_to_training_data, "r") as text, open(path_to_bin, "wb") as bin:
        bin.write((0).to_bytes(2, byteorder="little", signed=False))
        bin.write((0).to_bytes(2, byteorder="little", signed=False))
        i = 0
        # while (line := text.readline()) and i < 1000:
        while (line := text.readline()):
            i += 1
            tokens = encode(("a" + line).strip()[1:])
            for token in tokens:
                bin.write(token.to_bytes(2, byteorder="little", signed=False))
    print("done")
    with open(path_to_sections, "wb") as sections:
        for index in _section_indices:
            sections.write(index.to_bytes(4, byteorder="little", signed=False))
    with open(path_to_bin, "r+b") as bin:
        bin.write(_num_proofs.to_bytes(2, byteorder="little", signed=False))
        bin.write(_longest_section.to_bytes(2, byteorder="little", signed=False))
        # bytes = bin.read()
        # print(decode([int.from_bytes(bytes[i:i + 2], byteorder="little") for i in range(0, len(bytes), 2)]))

# generate_bin(os.path.join(os.path.dirname(__file__), "data.txt"), os.path.join(os.path.dirname(__file__), "data.bin"), os.path.join(os.path.dirname(__file__), "sections.bin"))

# print(f"INDEX_TO_TOKEN = {INDEX_TO_TOKEN}")
print(f"VOCAB_SIZE = {VOCAB_SIZE}")
# print(f"longest proof = {_longest_section}")
