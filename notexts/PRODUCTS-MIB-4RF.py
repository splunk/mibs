#
# PySNMP MIB module PRODUCTS-MIB-4RF (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/4rf/PRODUCTS-MIB-4RF
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:00 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
fourRFExperimental, fourRFModules, fourRFProducts = mibBuilder.importSymbols("MIB-4RF", "fourRFExperimental", "fourRFModules", "fourRFProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, ObjectIdentity, Integer32, Counter64, Unsigned32, enterprises, iso, NotificationType, IpAddress, MibIdentifier, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Integer32", "Counter64", "Unsigned32", "enterprises", "iso", "NotificationType", "IpAddress", "MibIdentifier", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fourRFProductsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 14817, 2, 2))
fourRFProductsModule.setRevisions(('2007-04-30 00:00', '2004-02-13 00:00',))
if mibBuilder.loadTexts: fourRFProductsModule.setLastUpdated('200704300000Z')
if mibBuilder.loadTexts: fourRFProductsModule.setOrganization('www.4rf.com')
fourRFCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 1))
if mibBuilder.loadTexts: fourRFCommon.setStatus('current')
fourRFAprisa = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 2))
if mibBuilder.loadTexts: fourRFAprisa.setStatus('current')
fourRFAprisaXE = ObjectIdentity((1, 3, 6, 1, 4, 1, 14817, 7, 3))
if mibBuilder.loadTexts: fourRFAprisaXE.setStatus('current')
mibBuilder.exportSymbols("PRODUCTS-MIB-4RF", PYSNMP_MODULE_ID=fourRFProductsModule, fourRFAprisaXE=fourRFAprisaXE, fourRFProductsModule=fourRFProductsModule, fourRFCommon=fourRFCommon, fourRFAprisa=fourRFAprisa)
