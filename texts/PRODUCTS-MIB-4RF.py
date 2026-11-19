#
# PySNMP MIB module PRODUCTS-MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/4rf/PRODUCTS-MIB-4RF
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:01 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fourRFExperimental, fourRFProducts, fourRFModules = mibBuilder.importSymbols("MIB-4RF", "fourRFExperimental", "fourRFProducts", "fourRFModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Counter32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, IpAddress, Unsigned32, ModuleIdentity, enterprises, Integer32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "IpAddress", "Unsigned32", "ModuleIdentity", "enterprises", "Integer32", "Counter64", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("PRODUCTS-MIB-4RF", fourRFAprisa=fourRFAprisa, fourRFCommon=fourRFCommon, PYSNMP_MODULE_ID=fourRFProductsModule, fourRFProductsModule=fourRFProductsModule, fourRFAprisaXE=fourRFAprisaXE)
