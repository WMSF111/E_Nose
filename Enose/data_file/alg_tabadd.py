from PySide6.QtWidgets import QDialog
import data_file.algriothm as algr
import resource_ui.alg_puifile.pic_tab_add as alg_show
import data_file.transfo as transfo

class ALG_TAB_ADD():
    def __init__(self, ui):
        self.ui = ui
        self.tabWidget = ui.tabWidget
        # 定义TAB类
        self.tabset = alg_show.ADDTAB(self.tabWidget)

    def Filter_Combo_select(self):
        pre_plot =alg_show.PRESHOW()
        if pre_plot.exec() == QDialog.Accepted:  # 等待弹窗关闭
            print(pre_plot.PreAlg, pre_plot.ValAlg)
            Dataframe = transfo.UI_TXT_TO.read_files_to_dataframe(pre_plot.file_path)  # 读取txt转数组
            if(pre_plot.PreAlg != "不选"):
                pre_alg = algr.Pre_Alg(self, Dataframe, pre_plot.PreAlg) #创建预处理算法对象
                result = pre_alg.Filter_Choose()
                print(result)
                # .strip()去除前后不必要空格
                self.tabset.add_text_tab(
                    finaldata=result,
                    title=f"{pre_plot.PreAlg}数据",
                    html = True)
                self.tabset.add_plot_tab(
                    title=f"{pre_plot.PreAlg}对比图",
                    plot_function=pre_plot.plot_data,
                    data = Dataframe,
                    plot_function2=pre_plot.plot_result,
                    result = result)
            if(pre_plot.ValAlg != "不选"):
                if(pre_plot.PreAlg != "不选"):
                    Dataframe = result # 对滤波后的数据进行处理
                pre_alg = algr.Pre_Alg(self, Dataframe, pre_plot.ValAlg)  # 创建选择数据对象
                val_text = pre_alg.Val_Choose()
                self.tabset.add_text_tab(
                    finaldata=val_text,
                    title=f"{pre_plot.ValAlg}数据",
                    html=True)

    def Di_Re_Combo_select(self, index):
        selected_item = self.ui.Classify_ComboBox.itemText(index)
        if selected_item == "PCA":
            pca = alg_show.PCASHOW()  # PCA弹窗
            self.process_data_and_plot(selected_item="PCA", dialog=pca, transfo=transfo,
                                       plot_title="PCA", plot_function=pca.plot_scree_plot)

        if selected_item == "LDA":
            lda = alg_show.LDASHOW()  # LDA弹窗
            self.process_data_and_plot(selected_item="LDA", dialog=lda, transfo=transfo,
                                       plot_title="LDA", plot_function=lda.plot_lda_variance_ratio)




    def Classify_Combo_select(self, index): #回归算法
        selected_item = self.ui.Reg_ComboBox.itemText(index)
        if (selected_item == "线性回归"):
            lr = alg_show.LRSHOW() # LR弹窗
            self.ui.Reg_ComboBox.setCurrentIndex(0)
            if lr.exec() == QDialog.Accepted:  # 等待弹窗关闭
                DataFrame = transfo.UI_TXT_TO.read_files_to_dataframe(lr.file_path)  # 读取txt转数组
                Target = DataFrame.iloc[1:, 0]
                # 将剩余的列作为数据 (features)
                Data = DataFrame.iloc[1:, 1:]
                train = algr.TRAIN(self.ui, Target, Data)
                accuracy, confusion, classification, err_str = train.LG_train(lr.desize)
                accuracy_str = err_str + "模型准确率:" + str(accuracy) + '\n'
                confusion_str = "混淆矩阵:\n" + "\n".join(" ".join(map(str, row)) for row in confusion)
                classification_str = "\n分类矩阵:\n  " + " ".join(map(str, classification))
                # 使用空格连接列表元素
                self.tabset.add_text_tab(
                    finaldata=accuracy_str + confusion_str + classification_str,
                    title="预测性能",
                    html=False
                )
                # 去除重复标签并保持原有顺序
                unique_labels = []
                for label in Target:
                    if label not in unique_labels:
                        unique_labels.append(label)
                self.tabset.add_plot_tab(
                    title="线性回归混淆矩阵",
                    plot_function = lr.plot_confusion,
                    confusion = confusion,
                    labels_name = list(set(unique_labels)))
        if selected_item == "SVM":
            svm_show = alg_show.SVMSHOW()  # SVM弹窗
            if svm_show.exec() == QDialog.Accepted:  # 等待弹窗关闭
                DataFrame = transfo.UI_TXT_TO.read_files_to_dataframe(svm_show.file_path)  # 读取txt转数组
                Target = DataFrame.iloc[1:, 0]
                # 将剩余的列作为数据 (features)
                Data = DataFrame.iloc[1:, 1:]
                S_class = algr.TRAIN(self.ui, Target, Data)  # 创建预处理算法对象
                X_combined_std, y_combined, svm, range = S_class.svm(svm_show.desize)
                self.tabset.add_plot_tab(
                    title=f"SVM混淆矩阵",
                    plot_function=svm_show.plot_decision_regions,
                    X = X_combined_std,
                    y = y_combined,
                    classifier = svm,
                    test_idx = range
                    )

    def process_data_and_plot(self, selected_item, dialog, transfo, plot_title, plot_function):
        self.ui.Classify_ComboBox.setCurrentIndex(0)
        if dialog.exec() == QDialog.Accepted:  # 等待弹窗关闭
            print("弹窗返回值:", dialog.Dinum, dialog.Contrnum)
            # 读取txt并显示到数据源看板
            DataFrame = transfo.UI_TXT_TO.read_files_to_dataframe(dialog.file_path)
            # 选择算法
            alg = algr.choose_alg(self.ui, DataFrame)

            # 根据选项进行PCA或LDA的计算
            if selected_item == "PCA":
                dataframe_data, variance_ratios = alg.pca(dialog.Dinum, dialog.Contrnum)
                # 碎石图
                self.tabset.add_plot_tab(
                    title="PCA 碎石图",
                    plot_function=plot_function,
                    variance_ratios=variance_ratios)
            elif selected_item == "LDA":
                dataframe_data, variance_ratios = alg.lda(dialog.Dinum, dialog.Contrnum)
                self.tabset.add_plot_tab(
                    title="LDA解释方差图",
                    plot_function=plot_function,
                    variance_ratios=variance_ratios,
                    Contrnum=dialog.Contrnum)

            # 原始数据
            self.tabset.add_text_tab(
                finaldata=DataFrame,
                title=f"{selected_item}原始数据",
                    html=True
            )

            self.tabset.add_text_tab(
                finaldata=dataframe_data,
                title=f"{selected_item}结果数据",
                    html=True
            )

            # 如果Dinum小于4，添加散点图
            if dialog.Dinum < 4:
                self.tabset.add_plot_tab(
                    Dnum=dialog.Dinum,
                    title=f"{selected_item} 散点图",
                    plot_function=alg_show.draw_scatter,
                    name=["1", "2", "3"],
                    num=dialog.Dinum,
                    target=DataFrame.iloc[:, 0].values,  # 通过索引0获取第一列的值,
                    finalData=alg.finalData # 计算后的值
                )


