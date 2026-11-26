#
# PySNMP MIB module CISCO-VOICE-APPLICATIONS-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-APPLICATIONS-OID-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceApplicationsOIDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 5))
ciscoVoiceApplicationsOIDMIB.setRevisions(('2004-06-17 00:00',))
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setLastUpdated('200406170000Z')
if mibBuilder.loadTexts: ciscoVoiceApplicationsOIDMIB.setOrganization('Cisco Systems, Inc.')
cvaMIBOids = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1))
ciscoCallManager = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 1))
ciscoCallManagerExpress = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 2))
ciscoSRST = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 3))
ciscoBTS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 4))
ciscoCSPS = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 5, 1, 5))
mibBuilder.exportSymbols("CISCO-VOICE-APPLICATIONS-OID-MIB", ciscoCallManagerExpress=ciscoCallManagerExpress, PYSNMP_MODULE_ID=ciscoVoiceApplicationsOIDMIB, ciscoSRST=ciscoSRST, ciscoCSPS=ciscoCSPS, cvaMIBOids=cvaMIBOids, ciscoBTS=ciscoBTS, ciscoVoiceApplicationsOIDMIB=ciscoVoiceApplicationsOIDMIB, ciscoCallManager=ciscoCallManager)
