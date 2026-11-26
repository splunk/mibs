#
# PySNMP MIB module CISCO-DMN-DSG-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-ROOT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSPVTG = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429))
ciscoSPVTG.setRevisions(('2010-08-30 11:00', '2009-11-26 15:00',))
if mibBuilder.loadTexts: ciscoSPVTG.setLastUpdated('201008301100Z')
if mibBuilder.loadTexts: ciscoSPVTG.setOrganization('Cisco Systems, Inc.')
ciscoSat = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2))
ciscoDMN = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2))
ciscoDSGUtilities = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5))
ciscoDSGProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 6))
mibBuilder.exportSymbols("CISCO-DMN-DSG-ROOT-MIB", ciscoDSGProducts=ciscoDSGProducts, ciscoSPVTG=ciscoSPVTG, ciscoDSGUtilities=ciscoDSGUtilities, ciscoSat=ciscoSat, ciscoDMN=ciscoDMN, PYSNMP_MODULE_ID=ciscoSPVTG)
