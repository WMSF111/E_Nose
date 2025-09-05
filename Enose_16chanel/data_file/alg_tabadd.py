from PySide6.QtWidgets import QDialog, QFileDialog
import data_file.algriothm as algriothm
import resource_ui.alg_puifile.pic_tab_add as alg_show
import global_var as glov
import data_file.transfo as transfo

class ALG_TAB_ADD():
    def __init__(self, ui):
        self.ui = ui
        self.tabWidget = ui.tabWidget
        # 定义TAB类
        self.tabset = alg_show.ADDTAB(self.tabWidget)

    def Di_Re_Combo_select(self, index):
        selected_item = self.ui.Di_Re_ComboBox.itemText(index)
        if(selected_item == "PCA"):
            pca = alg_show.PCASHOW()
            if pca.exec() == QDialog.Accepted:  # 等待弹窗关闭
                print("弹窗返回值:", pca.Dinum, pca.Contrnum)
                DataFrame = transfo.UI_TXT_TO.txt_to_dataframe(pca.file_path)  # 读取txt并显示到数据源看板
                alg = algriothm.choose_alg(self.ui, DataFrame)
                finaldata, variance_ratios = alg.pca(pca.Dinum, pca.Contrnum)
                self.tabset.add_text_tab(
                    finaldata=DataFrame.to_string(index=False),
                    title="原始数据"
                )
                str_finaldata = str(finaldata)
                self.tabset.add_text_tab(
                    finaldata = str_finaldata,
                    title="PCA结果数据"
                )
                self.tabset.add_plot_tab(
                    title="PCA 碎石图",
                    plot_function=pca.plot_scree_plot,
                    variance_ratios=variance_ratios)
                if pca.Dinum < 4:
                    self.tabset.add_plot_tab(
                        Dnum=pca.Dinum,
                        title="PCA 散点图",
                        plot_function=alg_show.draw_scatter,
                        name=["1", "2", "3"],
                        num=pca.Dinum,
                        target=DataFrame['target'].values,
                        finalData=finaldata
                )

        if (selected_item == "LDA"):
            lda = alg_show.LDASHOW()
            if lda.exec() == QDialog.Accepted:  # 等待弹窗关闭
                print("弹窗返回值:", lda.Dinum, lda.Contrnum)
                DataFrame = transfo.UI_TXT_TO.txt_to_dataframe(lda.file_path)  # 读取txt并显示到数据源看板
                alg = algriothm.choose_alg(self.ui, DataFrame)
                finaldata, variance_ratios = alg.lda(lda.Dinum, lda.Contrnum)
                str_finaldata = str(finaldata)
                self.tabset.add_text_tab(
                    finaldata=str_finaldata,
                    title="LDA结果数据"
                )
                self.tabset.add_plot_tab(
                    title="LDA解释方差图",
                    plot_function=lda.plot_lda_variance_ratio,
                    variance_ratios=variance_ratios,
                    Contrnum = lda.Contrnum)
                if lda.Dinum < 4:
                    self.tabset.add_plot_tab(
                        Dnum=lda.Dinum,
                        title="PCA 散点图",
                        plot_function=alg_show.draw_scatter,
                        name=["1", "2", "3"],
                        num=lda.Dinum,
                        target=DataFrame['target'].values,
                        finalData=finaldata
                    )

    def Classify_Combo_select(self, index):
        selected_item = self.ui.Classify_ComboBox.itemText(index)
        train = algriothm.TRAIN(self.ui)
        if (selected_item == "线性回归"):
            lr = alg_show.LRSHOW()
            print("弹窗返回值:", lr.desize)
            finaldata, variance_ratios = train.LG_train(lr.desize)
