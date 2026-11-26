#
# PySNMP MIB module CISCO-NAC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NAC-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNacTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 530))
ciscoNacTcMIB.setRevisions(('2006-05-31 00:00',))
if mibBuilder.loadTexts: ciscoNacTcMIB.setLastUpdated('200605310000Z')
if mibBuilder.loadTexts: ciscoNacTcMIB.setOrganization('Cisco Systems, Inc.')
class CnnEouState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("initialize", 1), ("hello", 2), ("clientless", 3), ("eapRequest", 4), ("response", 5), ("authenticated", 6), ("fail", 7), ("abort", 8), ("aaaFail", 9), ("hold", 10), ("client", 11), ("server", 12))

class CnnEouAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("clientless", 1), ("eap", 2), ("static", 3), ("unknown", 4))

class CnnEouDeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ciscoIpPhone", 1))

class CnnEouPostureToken(TextualConvention, Integer32):
    status = 'deprecated'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 1), ("healthy", 2), ("checkup", 3), ("quarantine", 4), ("infected", 5))

class CnnEouPostureTokenString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-NAC-TC-MIB", CnnEouAuthType=CnnEouAuthType, CnnEouPostureTokenString=CnnEouPostureTokenString, PYSNMP_MODULE_ID=ciscoNacTcMIB, CnnEouPostureToken=CnnEouPostureToken, CnnEouState=CnnEouState, ciscoNacTcMIB=ciscoNacTcMIB, CnnEouDeviceType=CnnEouDeviceType)
