#
# PySNMP MIB module BINTEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bintec/BINTEC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:33:59 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, enterprises, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, IpAddress, Integer32, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "enterprises", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "IpAddress", "Integer32", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
isdn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 2))
biboip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 5))
atm = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 16))
sys = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17))
admin_2 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 22)).setLabel("admin-2")
vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 23))
ipsec = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 26))
qos = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 27))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 30))
voip = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 33))
security = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 38))
vif = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 39))
tty = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 41))
ssh = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 44))
phy = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 45))
wlan = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 46))
ima = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 54))
usb = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 55))
resource = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 17, 4))
gui = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 69))
class PhysAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class Date(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class HexValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class BitValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("BINTEC-MIB", Timeout=Timeout, ima=ima, BridgeId=BridgeId, wlan=wlan, sys=sys, admin_2=admin_2, atm=atm, ipsec=ipsec, phy=phy, adsl=adsl, bibo=bibo, voip=voip, gui=gui, HexValue=HexValue, security=security, MacAddress=MacAddress, DisplayString=DisplayString, bintec=bintec, vpn=vpn, BitValue=BitValue, vif=vif, ssh=ssh, qos=qos, Date=Date, biboip=biboip, resource=resource, isdn=isdn, PhysAddress=PhysAddress, tty=tty, usb=usb)
