#
# PySNMP MIB module SWDGS1510PRIMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/SWDGS1510PRIMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlink_mgmt, dlink_products = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-mgmt", "dlink-products")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlink_Dgs1510Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137)).setLabel("dlink-Dgs1510Prod")
dlink_Dgs1510Prod_Dgs1510_20 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 1)).setLabel("dlink-Dgs1510Prod-Dgs1510-20")
dlink_Dgs1510Prod_Dgs1510_28 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 2)).setLabel("dlink-Dgs1510Prod-Dgs1510-28")
dlink_Dgs1510Prod_Dgs1510_28P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 3)).setLabel("dlink-Dgs1510Prod-Dgs1510-28P")
dlink_Dgs1510Prod_Dgs1510_52 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 4)).setLabel("dlink-Dgs1510Prod-Dgs1510-52")
dlink_Dgs1510Prod_Dgs1510_28X = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 6)).setLabel("dlink-Dgs1510Prod-Dgs1510-28X")
dlink_Dgs1510Prod_Dgs1510_52X = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 8)).setLabel("dlink-Dgs1510Prod-Dgs1510-52X")
dlink_Dgs1510Prod_Dgs1510_28XMP = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 9)).setLabel("dlink-Dgs1510Prod-Dgs1510-28XMP")
dlink_Dgs1510Prod_Dgs1510_52XMP = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 137, 10)).setLabel("dlink-Dgs1510Prod-Dgs1510-52XMP")
dlink_Dgs1510Proj = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118)).setLabel("dlink-Dgs1510Proj")
dlink_Dgs1510ProjModel = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1)).setLabel("dlink-Dgs1510ProjModel")
dlink_Dgs1510Proj_Dgs1510_20 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 1)).setLabel("dlink-Dgs1510Proj-Dgs1510-20")
dlink_Dgs1510Proj_Dgs1510_28 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 2)).setLabel("dlink-Dgs1510Proj-Dgs1510-28")
dlink_Dgs1510Proj_Dgs1510_28P = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 3)).setLabel("dlink-Dgs1510Proj-Dgs1510-28P")
dlink_Dgs1510Proj_Dgs1510_52 = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 4)).setLabel("dlink-Dgs1510Proj-Dgs1510-52")
dlink_Dgs1510Proj_Dgs1510_28X = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 6)).setLabel("dlink-Dgs1510Proj-Dgs1510-28X")
dlink_Dgs1510Proj_Dgs1510_52X = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 8)).setLabel("dlink-Dgs1510Proj-Dgs1510-52X")
dlink_Dgs1510Proj_Dgs1510_28XMP = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 9)).setLabel("dlink-Dgs1510Proj-Dgs1510-28XMP")
dlink_Dgs1510Proj_Dgs1510_52XMP = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 118, 1, 10)).setLabel("dlink-Dgs1510Proj-Dgs1510-52XMP")
mibBuilder.exportSymbols("SWDGS1510PRIMGMT-MIB", dlink_Dgs1510Prod_Dgs1510_28P=dlink_Dgs1510Prod_Dgs1510_28P, dlink_Dgs1510Proj=dlink_Dgs1510Proj, dlink_Dgs1510Prod_Dgs1510_52X=dlink_Dgs1510Prod_Dgs1510_52X, dlink_Dgs1510Prod_Dgs1510_52=dlink_Dgs1510Prod_Dgs1510_52, dlink_Dgs1510Proj_Dgs1510_20=dlink_Dgs1510Proj_Dgs1510_20, dlink_Dgs1510ProjModel=dlink_Dgs1510ProjModel, dlink_Dgs1510Prod_Dgs1510_28=dlink_Dgs1510Prod_Dgs1510_28, dlink_Dgs1510Proj_Dgs1510_28=dlink_Dgs1510Proj_Dgs1510_28, dlink_Dgs1510Proj_Dgs1510_28P=dlink_Dgs1510Proj_Dgs1510_28P, dlink_Dgs1510Proj_Dgs1510_28XMP=dlink_Dgs1510Proj_Dgs1510_28XMP, dlink_Dgs1510Prod=dlink_Dgs1510Prod, dlink_Dgs1510Proj_Dgs1510_28X=dlink_Dgs1510Proj_Dgs1510_28X, dlink_Dgs1510Proj_Dgs1510_52X=dlink_Dgs1510Proj_Dgs1510_52X, dlink_Dgs1510Prod_Dgs1510_28X=dlink_Dgs1510Prod_Dgs1510_28X, dlink_Dgs1510Prod_Dgs1510_52XMP=dlink_Dgs1510Prod_Dgs1510_52XMP, dlink_Dgs1510Proj_Dgs1510_52=dlink_Dgs1510Proj_Dgs1510_52, dlink_Dgs1510Prod_Dgs1510_28XMP=dlink_Dgs1510Prod_Dgs1510_28XMP, dlink_Dgs1510Proj_Dgs1510_52XMP=dlink_Dgs1510Proj_Dgs1510_52XMP, dlink_Dgs1510Prod_Dgs1510_20=dlink_Dgs1510Prod_Dgs1510_20)
