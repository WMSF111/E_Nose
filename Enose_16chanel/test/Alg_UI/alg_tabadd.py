from PySide6.QtWidgets import QDialog, QFileDialog
import algriothm as algriothm
import resource_ui.alg_puifile.pic_tab_add as alg_show
import global_var as glov
import transfo as transfo
import filter

class ALG_TAB_ADD():
    def __init__(self, ui):
        self.ui = ui
        self.tabWidget = ui.tabWidget
        # 定义TAB类
        self.tabset = alg_show.ADDTAB(self.tabWidget)

    def Filter_Combo_select(self):
        pre =alg_show.PRESHOW()
        if pre.exec() == QDialog.Accepted:  # 等待弹窗关闭
            print(pre.PreAlg, pre.ValAlg)
            Dataframe = transfo.UI_TXT_TO.txt_to_dataframe(pre.file_path)  # 读取txt转数组
            result = algriothm.Pre_Alg(self, Dataframe, pre.PreAlg)
            result_str = "\n".join(" ".join(map(str, row)) for row in result)
            self.tabset.add_text_tab(
                finaldata=result,
                title="预测性能"
            )


    def Di_Re_Combo_select(self, index):
        selected_item = self.ui.Classify_ComboBox.itemText(index)
        if selected_item == "PCA":
            pca = alg_show.PCASHOW()  # PCA弹窗
            self.process_data_and_plot(selected_item="PCA", dialog=pca, algriothm=algriothm, transfo=transfo,
                                       plot_title="PCA", plot_function=pca.plot_scree_plot, target_column_name="target")

        if selected_item == "LDA":
            lda = alg_show.LDASHOW()  # LDA弹窗
            self.process_data_and_plot(selected_item="LDA", dialog=lda, algriothm=algriothm, transfo=transfo,
                                       plot_title="LDA", plot_function=lda.plot_lda_variance_ratio,
                                       target_column_name="target")

    def Classify_Combo_select(self, index): #回归算法
        selected_item = self.ui.Reg_ComboBox.itemText(index)
        if (selected_item == "线性回归"):
            lr = alg_show.LRSHOW() # LR弹窗
            self.ui.Reg_ComboBox.setCurrentIndex(0)
            if lr.exec() == QDialog.Accepted:  # 等待弹窗关闭
                Target, Data = transfo.UI_TXT_TO.txt_to_Array(lr.file_path)  # 读取txt转数组
                train = algriothm.TRAIN(self.ui, Target, Data)
                accuracy, confusion, classification, err_str = train.LG_train(lr.desize)
                accuracy_str = err_str + "模型准确率:" + str(accuracy) + '\n'
                confusion_str = "混淆矩阵:\n" + "\n".join(" ".join(map(str, row)) for row in confusion)
                classification_str = "\n分类矩阵:\n  " + " ".join(map(str, classification))
                # 使用空格连接列表元素
                self.tabset.add_text_tab(
                    finaldata=accuracy_str + confusion_str + classification_str,
                    title="预测性能"
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

    def process_data_and_plot(self, selected_item, dialog, algriothm, transfo, plot_title, plot_function,
                              target_column_name):
        self.ui.Classify_ComboBox.setCurrentIndex(0)
        if dialog.exec() == QDialog.Accepted:  # 等待弹窗关闭
            print("弹窗返回值:", dialog.Dinum, dialog.Contrnum)
            # 读取txt并显示到数据源看板
            DataFrame = transfo.UI_TXT_TO.txt_to_dataframe(dialog.file_path)
            # 选择算法
            alg = algriothm.choose_alg(self.ui, DataFrame)

            # 根据选项进行PCA或LDA的计算
            if selected_item == "PCA":
                finaldata, variance_ratios = alg.pca(dialog.Dinum, dialog.Contrnum)
                # 碎石图
                self.tabset.add_plot_tab(
                    title="PCA 碎石图",
                    plot_function=plot_function,
                    variance_ratios=variance_ratios)
            elif selected_item == "LDA":
                finaldata, variance_ratios = alg.lda(dialog.Dinum, dialog.Contrnum)
                self.tabset.add_plot_tab(
                    title="LDA解释方差图",
                    plot_function=plot_function,
                    variance_ratios=variance_ratios,
                    Contrnum=dialog.Contrnum)

            # 原始数据
            self.tabset.add_text_tab(
                finaldata=DataFrame.to_string(index= False),
                title="原始数据"
            )

            # 将每行数据转化为字符串
            data_str = [" ".join(map(str, row)) for row in finaldata]
            # 将字符串列表转为最终的字符串（每行一个数据）
            final_str = "\n".join(data_str)
            self.tabset.add_text_tab(
                finaldata=final_str,
                title=f"{selected_item}结果数据"
            )

            # 转换为两列数据（如果有多列，取前两列）
            finaldata_columns = finaldata[:, 1:]
            # 如果Dinum小于4，添加散点图
            if dialog.Dinum < 4:
                self.tabset.add_plot_tab(
                    Dnum=dialog.Dinum,
                    title=f"{selected_item} 散点图",
                    plot_function=alg_show.draw_scatter,
                    name=["1", "2", "3"],
                    num=dialog.Dinum,
                    target=DataFrame[target_column_name].values,
                    finalData=finaldata_columns
                )


