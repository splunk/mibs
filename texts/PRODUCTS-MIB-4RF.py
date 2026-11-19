#
# PySNMP MIB module PRODUCTS-MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/4rf/PRODUCTS-MIB-4RF
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
fourRFExperimental, fourRFProducts, fourRFModules = mibBuilder.importSymbols("MIB-4RF", "fourRFExperimental", "fourRFProducts", "fourRFModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, TimeTicks, Gauge32, ModuleIdentity, NotificationType, MibIdentifier, enterprises, iso, IpAddress, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "TimeTicks", "Gauge32", "ModuleIdentity", "NotificationType", "MibIdentifier", "enterprises", "iso", "IpAddress", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fourRFProductsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 14817, 2, 2))
fourRFProductsModule.setRevisions(('2007-04-30 00:00', '2004-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fourRFProductsModule.setRevisionsDescriptions(('Second draft', 'First draft',))
if mibBuilder.loadTexts: fourRFProductsModule.setLastUpdated('200704300000Z')
if mibBuilder.loadTexts: fourRFProductsModule.setOrganization('www.4rf.com')
if mibBuilder.loadTexts: fourRFProductsModule.setContactInfo('postal:   4RF Communications Ltd\n                    26 Glover Street\n                    Ngauranga\n                    PO Box 13-506\n                    Wellington 6032\n                    New Zealand\n                    \n          phone:    +64 4 499 6000\n          email:    support@4rf.com')
if mibBuilder.loadTexts: fourRFProductsModule.setDescription('4RF product registrations, all 4RF SNMP managed products have\n         a root identifier specified here.')
fourRFCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 1))
if mibBuilder.loadTexts: fourRFCommon.setStatus('current')
if mibBuilder.loadTexts: fourRFCommon.setDescription('Sub-tree for common elements.')
fourRFAprisa = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 2))
if mibBuilder.loadTexts: fourRFAprisa.setStatus('current')
if mibBuilder.loadTexts: fourRFAprisa.setDescription('Sub-tree for Aprisa/AprisaView.')
fourRFAprisaXE = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 3))
if mibBuilder.loadTexts: fourRFAprisaXE.setStatus('current')
if mibBuilder.loadTexts: fourRFAprisaXE.setDescription('Sub-tree for AprisaXE.')
mibBuilder.exportSymbols("PRODUCTS-MIB-4RF", fourRFAprisaXE=fourRFAprisaXE, PYSNMP_MODULE_ID=fourRFProductsModule, fourRFCommon=fourRFCommon, fourRFAprisa=fourRFAprisa, fourRFProductsModule=fourRFProductsModule)
